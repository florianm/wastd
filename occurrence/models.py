# -*- coding: utf-8 -*-
"""Occurrence models.

These models support opportunistic encounters with threatened and priority
Fauna, Flora and Comunities (defined in taxonomy).

Observer name / address / phone / email is captured through the observer being
a system user.
"""
from __future__ import unicode_literals, absolute_import

# import itertools
import logging
# import os
# import urllib
# import slugify
# from datetime import timedelta
# from dateutil import tz

# from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_delete, pre_save, post_save  # noqa
from django.dispatch import receiver
from django.contrib.gis.db import models as geo_models
# from django.contrib.gis.db.models.query import GeoQuerySet
from django.urls import reverse
# from rest_framework.reverse import reverse as rest_reverse
from django.template import loader
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe

# from durationfield.db.models.fields.duration import DurationField
# from django.db.models.fields import DurationField
# from django_fsm import FSMField, transition
# from django_fsm_log.decorators import fsm_log_by
# from django_fsm_log.models import StateLog
from polymorphic.models import PolymorphicModel

# from wastd.users.models import User
from shared.models import (LegacySourceMixin,
                           ObservationAuditMixin,
                           QualityControlMixin)
from taxonomy.models import Taxon, Community

logger = logging.getLogger(__name__)


class AreaEncounter(PolymorphicModel,
                    LegacySourceMixin,
                    ObservationAuditMixin,
                    QualityControlMixin,
                    geo_models.Model):
    """An Encounter with an Area.

    The Area is represented spatially throuh a polygonal extent
    and an additional point.

    This model accommodates anything with a spatial extent, providing:

    * Area type (to classify different kinds of areas)
    * Area code to identify multiple measurements of the same Area
    * Polygonal or Point representation of the area
    * Mixins: data QA levels, legacy source tracking

    Some additional fields are populated behind the scenes at each save and
    serve to cache low churn, high use content:

    * label: the cached __str__ representation
    * point: set from geom centroid id empty
    * northern extent: useful to sort Areas by latitude
    * as html: a pre-compiled HTML map popup
    """

    AREA_TYPE_EPHEMERAL_SITE = 0
    AREA_TYPE_PERMANENT_SITE = 1
    AREA_TYPE_CRITICAL_HABITAT = 2
    AREA_TYPE_TEC_BOUNDARY = 10
    AREA_TYPE_TEC_BUFFER = 11
    AREA_TYPE_TEC_SITE = 12
    AREA_TYPE_FLORA_POPULATION = 20
    AREA_TYPE_FLORA_SUBPOPULATION = 21
    AREA_TYPE_FAUNA_SITE = 30
    AREA_TYPE_MPA = 40
    AREA_TYPE_LOCALITY = 41

    AREA_TYPES = (
        (AREA_TYPE_EPHEMERAL_SITE, "Ephemeral Site"),
        (AREA_TYPE_PERMANENT_SITE, "Permanent Site"),
        (AREA_TYPE_CRITICAL_HABITAT, "Critical Habitat"),
        (AREA_TYPE_TEC_BOUNDARY, "TEC Boundary"),
        (AREA_TYPE_TEC_BUFFER, "TEC Buffer"),
        (AREA_TYPE_TEC_SITE, "TEC Site"),
        (AREA_TYPE_FLORA_POPULATION, "Flora Population"),
        (AREA_TYPE_FLORA_SUBPOPULATION, "Flora Subpopulation"),
        (AREA_TYPE_FAUNA_SITE, "Fauna Site"),
        (AREA_TYPE_MPA, "Marine Protected Area"),
        (AREA_TYPE_LOCALITY, "Locality"),
    )

    # Naming -----------------------------------------------------------------#
    code = models.CharField(
        max_length=1000,
        blank=True, null=True,
        verbose_name=_("Area code"),
        help_text=_("A URL-safe, short code for the area. "
                    "Multiple records of the same Area "
                    "will be recognised by the same area type and code."),
    )

    label = models.CharField(
        blank=True, null=True,
        max_length=1000,
        editable=False,
        verbose_name=_("Label"),
        help_text=_("A short but comprehensive label for the encounter, "
                    "populated from the model's string representation."),
    )

    name = models.CharField(
        blank=True, null=True,
        max_length=1000,
        verbose_name=_("Area name"),
        help_text=_("A human-readable name for the observed area."),
    )

    description = models.TextField(
        blank=True, null=True,
        verbose_name=_("Description"),
        help_text=_("A comprehensive description."),
    )

    # Time: ObservationAuditMixin provides date and observer -----------------#
    #
    # Geolocation ------------------------------------------------------------#
    area_type = models.PositiveIntegerField(
        verbose_name=_("Area type"),
        default=AREA_TYPE_EPHEMERAL_SITE,
        choices=AREA_TYPES,
        help_text=_("The area type."), )

    accuracy = models.FloatField(
        blank=True, null=True,
        verbose_name=_("Accuracy [m]"),
        help_text=_("The measured or estimated accuracy of the location in meters."),
    )

    point = geo_models.PointField(
        srid=4326,
        blank=True, null=True,
        verbose_name=_("Representative Point"),
        help_text=_("A Point representing the Area."
                    " If empty, the centroid will be calculated from the Area's polygon extent."))

    northern_extent = models.FloatField(
        verbose_name=_("Northernmost latitude"),
        editable=False,
        blank=True, null=True,
        help_text=_("The northernmost latitude serves to sort areas."),)

    geom = geo_models.PolygonField(
        srid=4326,
        blank=True, null=True,
        verbose_name=_("Location"),
        help_text=_("The exact extent of the area as polygon in WGS84, if available."))

    # Cached fields ----------------------------------------------------------#
    as_html = models.TextField(
        verbose_name=_("HTML representation"),
        blank=True, null=True, editable=False,
        help_text=_("The cached HTML representation for display purposes."),)

    class Meta:
        """Class options."""

        ordering = ["-northern_extent", "name"]
        verbose_name = "Area Encounter"
        verbose_name_plural = "Area Encounters"

    def __str__(self):
        """The unicode representation."""
        return "Encounter at [{0}] ({1}) {2} on {3} by {4}".format(
            self.get_area_type_display(),
            self.code,
            self.name,
            self.encountered_on,
            self.encountered_by)

    @property
    def derived_point(self):
        """The point, derived from the polygon."""
        if self.geom:
            return self.geom.centroid
        else:
            return None

    @property
    def derived_northern_extent(self):
        """The northern extent, derived from the polygon."""
        if self.geom:
            return self.geom.extent[3]
        elif self.point:
            return self.point.y
        else:
            return None

    @property
    def absolute_admin_url(self):
        """Return the absolute admin change URL."""
        return reverse('admin:{0}_{1}_change'.format(
            self._meta.app_label, self._meta.model_name), args=[self.pk])

    @property
    def derived_html(self):
        """Generate HTML popup content."""
        template = "occurrence/popup/{0}.html".format(self._meta.model_name)
        try:
            t = loader.get_template(template)
            return mark_safe(t.render({"original": self}))
        except:
            logger.info("[occurrence.models.{0}] Template missing: {1}".format(self._meta.model_name, template))
            return self.__str__()

    def get_nearby_encounters(self, dist_dd=0.005):
        """Get encounters within dist_dd (default 0.005 degrees, ca 500m).

        Arguments:

        dist_dd <float> The search radius in decimal degrees. Default: 0.005 (ca 500 m).

        Returns:
        A queryset of nearby AreaEncounters.
        """
        return AreaEncounter.objects.filter(point__distance_lte=(self.point, dist_dd))


@python_2_unicode_compatible
class TaxonAreaEncounter(AreaEncounter):
    """An Encounter in time and space with a Taxon."""

    taxon = models.ForeignKey(Taxon, on_delete=models.CASCADE, related_name="taxon_occurrences")

    class Meta:
        """Class options."""

        verbose_name = "Taxon Encounter"
        verbose_name_plural = "Taxon Encounters"

    def __str__(self):
        """The unicode representation."""
        return "Encounter of {5} at [{0}] ({1}) {2} on {3} by {4}".format(
            self.get_area_type_display(),
            self.code,
            self.name,
            self.encountered_on,
            self.encountered_by,
            self.taxon)

    def nearby_same(self, dist_dd=0.005):
        """Return encounters with same taxon within search radius (dist_dd).

        Arguments:

        dist_dd <float> The search radius in decimal degrees. Default: 0.005 (ca 500 m).

        Returns:
        A queryset of nearby TaxonAreaEncounters.
        """
        return TaxonAreaEncounter.objects.filter(
            taxon=self.taxon,
            point__distance_lte=(self.point, dist_dd)
        )


@python_2_unicode_compatible
class CommunityAreaEncounter(AreaEncounter):
    """An Encounter in time and space with a community."""

    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="community_occurrences")

    class Meta:
        """Class options."""

        verbose_name = "Community Encounter"
        verbose_name_plural = "Community Encounters"

    def __str__(self):
        """The unicode representation."""
        return "Encounter of {5} at [{0}] ({1}) {2} on {3} by {4}".format(
            self.get_area_type_display(),
            self.code,
            self.name,
            self.encountered_on,
            self.encountered_by,
            self.community)

    def nearby_same(self, dist_dd=0.005):
        """Return encounters with same community within search radius (dist_dd).

        Arguments:

        dist_dd <float> The search radius in decimal degrees. Default: 0.005 (ca 500 m).

        Returns:
        A queryset of nearby CommunityAreaEncounters.
        """
        return CommunityAreaEncounter.objects.filter(
            community=self.community,
            point__distance_lte=(self.point, dist_dd)
        )


@receiver(pre_save, sender=TaxonAreaEncounter)
@receiver(pre_save, sender=CommunityAreaEncounter)
def area_caches(sender, instance, *args, **kwargs):
    """AreaEncounter: Cache expensive lookups."""
    if instance.pk:
        logger.info("[area_caches] Updating cache fields.")
        instance.label = instance.__str__()
        if not instance.point:
            instance.point = instance.derived_point
        instance.northern_extent = instance.derived_northern_extent
        instance.as_html = instance.derived_html
    else:
        logger.info("[area_caches] New Area, re-save to populate caches.")

    # FAUNA ENC
    # Survey
    # Threats
    # Habitat and habitat conditions
    # Fire history
    # Vegetation class
    # Associated species
    # mgmt actions required
    # comments
    # DRF permit no
    # TaxonSpecimenEncounter
    # TaxonSampleEncounter

    # FLORA ENC
    # Survey: often no survey as most fauna enc are opportunistic
    # Threats
    # Habitat and habitat conditions
    # Fire history
    # Vegetation class
    # Associated species: mostly empty, flora
    # mgmt actions required
    # comments
    # DRF permit no
    # TaxonSpecimenEncounter
    # TaxonSampleEncounter

    # COM ENC
    # Survey: often no survey as most fauna enc are opportunistic
    # Threats
    # Habitat and habitat conditions
    # Fire history
    # Vegetation class
    # Associated species: mostly empty, flora
    # mgmt actions required
    # comments
    # DRF permit no
    # TaxonSpecimenEncounter
    # TaxonSampleEncounter
