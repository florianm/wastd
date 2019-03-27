# -*- coding: utf-8 -*-
"""Occurrence view test suite testing URLs, templates, and views."""
from __future__ import unicode_literals

from django.utils import timezone


from django.contrib.auth import get_user_model
from django.contrib.gis.geos import GEOSGeometry  # Point, Polygon
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from model_mommy import mommy
from mommy_spatial_generators import MOMMY_SPATIAL_FIELDS  # noqa
from occurrence import models as occ_models
from taxonomy.models import Community, Taxon  # noqa
# from django.contrib.contenttypes.models import ContentType

MOMMY_CUSTOM_FIELDS_GEN = MOMMY_SPATIAL_FIELDS


class CommunityAreaEncounterTests(TestCase):
    """CommunityAreaEncounter and related ObservationGroup tests."""

    def setUp(self):
        """Shared objects.

        Bugs with TestMommy vs django-polymorphic:
        https://github.com/django-polymorphic/django-polymorphic/issues/280
        https://github.com/django-polymorphic/django-polymorphic/issues/109


          polymorphic/models.py", line 112, in get_real_instance_class
          and not issubclass(model, self.__class__._meta.proxy_for_model):
          TypeError: issubclass() arg 2 must be a class or tuple of classes
        """
        self.com0 = mommy.make(
            Community,
            code="code0",
            name="name0",
            _fill_optional=['eoo'])
        self.com0.save()

        self.com1 = mommy.make(
            Community,
            code="code1",
            name="name1",
            _fill_optional=['eoo'])
        self.com1.save()

        self.taxon0 = mommy.make(
            Taxon,
            name_id=1000,
            name="name0",
            _fill_optional=['rank', 'eoo'])
        self.taxon0.save()

        self.user = get_user_model().objects.create_superuser(
            username="superuser",
            email="super@gmail.com",
            password="test")
        self.user.save()

        self.cae = occ_models.CommunityAreaEncounter.objects.create(
            community=self.com0,
            encountered_on=timezone.now(),
            encountered_by=self.user,
            point=GEOSGeometry('POINT (115 -32)', srid=4326)
        )

        self.fatt = occ_models.FileAttachment.objects.create(
            encounter=self.cae,
            attachment=SimpleUploadedFile('testfile.txt', b'These are the file contents.'),
            title="test",
            author=self.user
        )
        self.fatt.save()

        self.asssp1 = occ_models.AssociatedSpecies.objects.create(
            encounter=self.cae,
            taxon=self.taxon0
        )
        self.asssp1.save()

        self.fh1 = occ_models.FireHistory.objects.create(
            encounter=self.cae,
            last_fire_date=timezone.now().date(),
            fire_intensity=occ_models.FireHistory.HMLN_HIGH
        )
        self.fh1.save()

        self.aa0 = occ_models.AreaAssessment.objects.create(
            encounter=self.cae,
            area_surveyed_m2=None,
            survey_duration_min=None
        )
        self.aa0.save()

        self.aa1 = occ_models.AreaAssessment.objects.create(
            encounter=self.cae,
            area_surveyed_m2=200,
            survey_duration_min=None
        )
        self.aa1.save()

        self.aa2 = occ_models.AreaAssessment.objects.create(
            encounter=self.cae,
            area_surveyed_m2=532,
            survey_duration_min=47
        )
        self.aa2.save()

        self.client.force_login(self.user)

    def test_cae_absolute_admin_url_loads(self):
        """Test CommunityAreaEncounter absolute_admin_url."""
        response = self.client.get(self.cae.absolute_admin_url)
        self.assertEqual(response.status_code, 200)

    def test_cae_list_url_loads(self):
        """Test that CommunityAreaEncounter list_url is com detail url and loads."""
        self.assertEqual(self.cae.list_url(), reverse('occurrence:communityareaencounter-list'))

        response = self.client.get(self.cae.list_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'occurrence/areaencounter_list.html')

    def test_cae_detail_url_loads(self):
        """Test CommunityAreaEncounter detail_url."""
        url = reverse('occurrence:communityareaencounter-detail',
                      kwargs={'pk': self.cae.pk})
        self.assertEqual(url, self.cae.get_absolute_url())

        response = self.client.get(self.cae.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'occurrence/cards/firehistory.html')
        self.assertTemplateUsed(response, 'occurrence/cards/areaassessment.html')
        self.assertTemplateUsed(response, 'occurrence/cards/fileattachment.html')

    def test_community_detail_url_loads(self):
        """Test Community detail_url."""
        response = self.client.get(self.cae.community.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_cae_update_url_loads(self):
        """Test CommunityAreaEncounter update_url."""
        url = reverse('occurrence:communityareaencounter-update',
                      kwargs={'pk': self.cae.pk})
        self.assertEqual(url, self.cae.update_url)

        response = self.client.get(self.cae.update_url)
        self.assertEqual(response.status_code, 200)

    def test_cae_create_url_loads(self):
        """Test CommunityAreaEncounter create_url."""
        url = reverse('occurrence:communityareaencounter-create')
        self.assertEqual(url, occ_models.CommunityAreaEncounter.create_url())

        response = self.client.get(occ_models.CommunityAreaEncounter.create_url())
        self.assertEqual(response.status_code, 200)

    # ------------------------------------------------------------------------#
    # CAE AssociatedSpeciesObservation
    def test_asssp_absolute_admin_url_loads(self):
        """Test AssociatedSpeciesObservation absolute_admin_url."""
        response = self.client.get(self.asssp1.absolute_admin_url)
        self.assertEqual(response.status_code, 200)

    def test_asssp_detail_url_loads(self):
        """Test AssociatedSpeciesObservation get_absolute_url()."""
        response = self.client.get(self.asssp1.get_absolute_url())
        self.assertEqual(self.asssp1.get_absolute_url(), self.asssp1.encounter.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_asssp_update_url_loads(self):
        """Test AssociatedSpeciesObservation update_url."""
        response = self.client.get(self.asssp1.update_url)
        self.assertEqual(response.status_code, 200)

    # ------------------------------------------------------------------------#
    # CAE FireHistoryObservation
    def test_fh_absolute_admin_url_loads(self):
        """Test FireHistoryObservation absolute_admin_url."""
        response = self.client.get(self.fh1.absolute_admin_url)
        self.assertEqual(response.status_code, 200)

    def test_fh_detail_url_loads(self):
        """Test FireHistoryObservation get_absolute_url()."""
        response = self.client.get(self.fh1.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_fh_update_url_loads(self):
        """Test FireHistoryObservation update_url."""
        response = self.client.get(self.fh1.update_url)
        self.assertEqual(response.status_code, 200)

    # ------------------------------------------------------------------------#
    # TAE AreaAssessmentObservation
    def test_aa_absolute_admin_url_loads(self):
        """Test AreaAssessmentObservation absolute_admin_url."""
        response = self.client.get(self.aa0.absolute_admin_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.get(self.aa1.absolute_admin_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.get(self.aa2.absolute_admin_url)
        self.assertEqual(response.status_code, 200)

    def test_aa_detail_url_loads(self):
        """Test AreaAssessmentObservation get_absolute_url."""
        response = self.client.get(self.aa0.get_absolute_url())
        self.assertEqual(response.status_code, 200)

        response = self.client.get(self.aa1.get_absolute_url())
        self.assertEqual(response.status_code, 200)

        response = self.client.get(self.aa2.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_aa_update_url_loads(self):
        """Test AreaAssessmentObservation update_url."""
        response = self.client.get(self.aa0.update_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.get(self.aa1.update_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.get(self.aa2.update_url)
        self.assertEqual(response.status_code, 200)


class TaxonAreaEncounterTests(TestCase):
    """TaxonAreaEncounter and related ObservationGroup tests."""

    def setUp(self):
        """Shared objects.

        Bugs with TestMommy vs django-polymorphic:
        https://github.com/django-polymorphic/django-polymorphic/issues/280
        https://github.com/django-polymorphic/django-polymorphic/issues/109


          polymorphic/models.py", line 112, in get_real_instance_class
          and not issubclass(model, self.__class__._meta.proxy_for_model):
          TypeError: issubclass() arg 2 must be a class or tuple of classes
        """
        self.taxon0 = mommy.make(
            Taxon,
            name_id=1000,
            name="name0",
            _fill_optional=['rank', 'eoo'])
        self.taxon0.save()

        self.taxon1 = mommy.make(
            Taxon,
            name_id=1001,
            name="name1",
            _fill_optional=['rank', 'eoo'])
        self.taxon1.save()

        self.taxon2 = mommy.make(
            Taxon,
            name_id=1002,
            name="name2",
            _fill_optional=['rank', 'eoo'])
        self.taxon2.save()

        self.user = get_user_model().objects.create_superuser(
            username="superuser",
            email="super@gmail.com",
            password="test")
        self.user.save()

        self.tae = occ_models.TaxonAreaEncounter.objects.create(
            taxon=self.taxon0,
            encountered_on=timezone.now(),
            encountered_by=self.user,
            point=GEOSGeometry('POINT (115 -32)', srid=4326)
        )

        self.asssp1 = occ_models.AssociatedSpecies.objects.create(
            encounter=self.tae,
            taxon=self.taxon1
        )
        self.asssp1.save()

        self.asssp2 = occ_models.AssociatedSpecies.objects.create(
            encounter=self.tae,
            taxon=self.taxon2
        )
        self.asssp2.save()

        self.fh1 = occ_models.FireHistory.objects.create(
            encounter=self.tae,
            last_fire_date=timezone.now(),
            fire_intensity=occ_models.FireHistory.HMLN_HIGH
        )
        self.fh1.save()

        self.fatt = occ_models.FileAttachment.objects.create(
            encounter=self.tae,
            attachment=SimpleUploadedFile(
                'testfile.txt', b'These are the file contents.'),
            title="test",
            author=self.user
        )
        self.fatt.save()

        self.aa0 = occ_models.AreaAssessment.objects.create(
            encounter=self.tae,
            area_surveyed_m2=None,
            survey_duration_min=None
        )
        self.aa0.save()

        self.aa1 = occ_models.AreaAssessment.objects.create(
            encounter=self.tae,
            area_surveyed_m2=200,
            survey_duration_min=None
        )
        self.aa1.save()

        self.aa2 = occ_models.AreaAssessment.objects.create(
            encounter=self.tae,
            area_surveyed_m2=532,
            survey_duration_min=47
        )
        self.aa2.save()

        self.client.force_login(self.user)

    def test_home_loads(self):
        """Test index page."""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_map_loads(self):
        """Test map page."""
        response = self.client.get(reverse("map"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/home.html')

    def test_tae_absolute_admin_url_loads(self):
        """Test absolute admin url."""
        response = self.client.get(self.tae.absolute_admin_url)
        self.assertEqual(response.status_code, 200)

    def test_taxon_detail_url_loads(self):
        """Test Taxon detail_url."""
        response = self.client.get(self.tae.taxon.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_tae_list_url_loads(self):
        """Test that TaxonAreaEncounter list_url is taxon detail url and loads."""
        self.assertEqual(self.tae.list_url(), reverse('occurrence:taxonareaencounter-list'))

        response = self.client.get(self.tae.list_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'occurrence/areaencounter_list.html')

        self.assertContains(response, self.taxon0.name)

    def test_tae_detail_url_loads(self):
        """Test taxon detail url works and loads."""
        detail_url_constructed = reverse('occurrence:taxonareaencounter-detail',
                                         kwargs={'pk': self.tae.pk})
        self.assertEqual(detail_url_constructed, self.tae.get_absolute_url())

        response = self.client.get(self.tae.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.taxon0.name)
        self.assertContains(response, self.fatt.title)
        self.assertContains(response, self.fatt.author)
        self.assertTemplateUsed(response, 'occurrence/taxonareaencounter_detail.html')
        self.assertTemplateUsed(response, 'occurrence/cards/firehistory.html')
        self.assertTemplateUsed(response, 'occurrence/cards/areaassessment.html')
        self.assertTemplateUsed(response, 'occurrence/cards/fileattachment.html')

    def test_tae_update_url_loads(self):
        """Test taxon update url works and loads."""
        update_url_constructed = reverse('occurrence:taxonareaencounter-update',
                                         kwargs={'pk': self.tae.pk})
        self.assertEqual(update_url_constructed, self.tae.update_url)

        response = self.client.get(self.tae.update_url)
        self.assertEqual(response.status_code, 200)

    # ------------------------------------------------------------------------#
    # TAE AssociatedSpeciesObservation
    def test_asssp_absolute_admin_url_loads(self):
        """Test AssociatedSpeciesObservation absolute_admin_url."""
        url = self.asssp1.absolute_admin_url
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_asssp_detail_url_loads(self):
        """Test AssociatedSpeciesObservation get_absolute_url."""
        response = self.client.get(self.asssp1.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_asssp_update_url_loads(self):
        """Test AssociatedSpeciesObservation update_url."""
        response = self.client.get(self.asssp1.update_url)
        self.assertEqual(response.status_code, 200)

    # ------------------------------------------------------------------------#
    # TAE FireHistoryObservation
    def test_fh_absolute_admin_url_loads(self):
        """Test FireHistoryObservation absolute_admin_url."""
        response = self.client.get(self.fh1.absolute_admin_url)
        self.assertEqual(response.status_code, 200)

    def test_fh_detail_url_loads(self):
        """Test FireHistoryObservation get_absolute_url."""
        response = self.client.get(self.fh1.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_fh_update_url_loads(self):
        """Test FireHistoryObservation update_url."""
        response = self.client.get(self.fh1.update_url)
        self.assertEqual(response.status_code, 200)

    # ------------------------------------------------------------------------#
    # TAE FileAttachmentObservation
    def test_fatt_absolute_admin_url_loads(self):
        """Test FileAttachmentObservation absolute_admin_url."""
        response = self.client.get(self.fatt.absolute_admin_url)
        self.assertEqual(response.status_code, 200)

    def test_fatt_detail_url_loads(self):
        """Test FileAttachmentObservation get_absolute_url."""
        response = self.client.get(self.fatt.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_fatt_update_url_loads(self):
        """Test FileAttachmentObservation update_url."""
        response = self.client.get(self.fatt.update_url)
        self.assertEqual(response.status_code, 200)

    # ------------------------------------------------------------------------#
    # TAE AreaAssessmentObservation
    def test_aa_absolute_admin_url_loads(self):
        """Test AreaAssessmentObservation absolute_admin_url."""
        response = self.client.get(self.aa0.absolute_admin_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.get(self.aa1.absolute_admin_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.get(self.aa2.absolute_admin_url)
        self.assertEqual(response.status_code, 200)

    def test_aa_detail_url_loads(self):
        """Test AreaAssessmentObservation get_absolute_url."""
        response = self.client.get(self.aa0.get_absolute_url())
        self.assertEqual(response.status_code, 200)

        response = self.client.get(self.aa1.get_absolute_url())
        self.assertEqual(response.status_code, 200)

        response = self.client.get(self.aa2.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_aa_update_url_loads(self):
        """Test AreaAssessmentObservation update_url."""
        response = self.client.get(self.aa0.update_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.get(self.aa1.update_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.get(self.aa2.update_url)
        self.assertEqual(response.status_code, 200)
