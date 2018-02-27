# -*- coding: utf-8 -*-
"""Admin module for wastd.observations."""
from __future__ import absolute_import, unicode_literals

# from leaflet.admin import LeafletGeoAdmin
from leaflet.forms.widgets import LeafletWidget

# from django import forms as django_forms
import floppyforms as ff
from django.contrib import admin
from mptt.admin import MPTTModelAdmin, TreeRelatedFieldListFilter
# from django.contrib.gis import forms
from django.contrib.gis.db import models as geo_models

from django.utils.translation import ugettext_lazy as _
from easy_select2 import select2_modelform as s2form
# from easy_select2.widgets import Select2
from fsm_admin.mixins import FSMTransitionMixin
from reversion.admin import VersionAdmin

from taxonomy.models import (HbvName, HbvSupra, HbvGroup, HbvFamily,
                             HbvGenus, HbvSpecies, HbvVernacular, HbvXref, Taxon)
# from wastd.observations.filters import LocationListFilter
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ('user',)


@admin.register(HbvName)
class HbvNameAdmin(VersionAdmin, admin.ModelAdmin):
    """Admin for HbvName."""

    save_on_top = True
    # date_hierarchy = 'datetime'
    list_display = (
        'name_id', 'rank_name', 'full_name', 'vernacular', 'all_vernaculars',
        'author', 'reference', 'naturalised_status', 'naturalised_certainty',
        'is_eradicated', 'informal', 'is_current', 'comments',
        'added_by', 'added_on', 'updated_by', 'updated_on',
    )
    list_filter = (
        'rank_name', 'is_current', 'naturalised_status', 'naturalised_certainty',
        'is_eradicated', 'informal',
    )
    search_fields = (
        'name_id', 'name', 'full_name', 'vernacular', 'all_vernaculars', 'author')
    # autocomplete_lookup_fields = {'fk': ['handler', 'recorder', ], }

    # def type_display(self, obj):
    #     """Make tag type human readable."""
    #     return obj.get_tag_type_display()
    # type_display.short_description = 'Tag Type'


@admin.register(HbvSupra)
class HbvSupraAdmin(VersionAdmin, admin.ModelAdmin):
    """Admin for HbvSupra."""

    save_on_top = True
    # date_hierarchy = 'updated_on'
    list_display = ('supra_code', 'supra_name', 'updated_on', 'ogc_fid', )
    # list_filter = ('rank_name', )
    search_fields = ('supra_name', 'supra_code', )


@admin.register(HbvGroup)
class HbvGroupAdmin(VersionAdmin, admin.ModelAdmin):
    """Admin for HbvGroup."""

    save_on_top = True
    # date_hierarchy = 'updated_on'
    list_display = ('class_id', 'rank_name', 'name', 'name_id',
                    'updated_by', 'updated_on', 'ogc_fid', 'md5_rowhash')
    list_filter = ('class_id', )
    search_fields = ('rank_name', 'name', 'name_id',)


@admin.register(HbvFamily)
class HbvFamilyAdmin(VersionAdmin, admin.ModelAdmin):
    """Admin for HbvFamily."""

    save_on_top = True
    # date_hierarchy = 'updated_on'
    list_display = ('name_id',
                    'kingdom_name', 'division_name',
                    'class_name', 'order_name', 'family_name',
                    'author', 'editor', 'reference', 'comments',
                    'is_current', 'informal', 'added_on', 'updated_on',
                    'ogc_fid', 'md5_rowhash')
    list_filter = ('is_current', 'informal', )
    search_fields = ('kingdom_name', 'division_name',
                     'class_name', 'order_name', 'family_name', 'name_id', )


@admin.register(HbvGenus)
class HbvGenusAdmin(VersionAdmin, admin.ModelAdmin):
    """Admin for HbvGenus."""

    save_on_top = True
    # date_hierarchy = 'updated_on'
    list_display = ('name_id',
                    'kingdom_id', 'family_nid', 'genus',
                    'author', 'editor', 'reference', 'comments',
                    'is_current', 'informal',
                    'added_on', 'updated_on',
                    'ogc_fid', 'md5_rowhash')
    list_filter = ('is_current', 'informal', 'kingdom_id',)
    search_fields = ('genus', 'name_id', 'author')


@admin.register(HbvSpecies)
class HbvSpeciesAdmin(VersionAdmin, admin.ModelAdmin):
    """Admin for HbvSpecies."""

    save_on_top = True
    # date_hierarchy = 'updated_on'
    list_display = ('name_id',
                    "species_name", "species_code",
                    "consv_code", "ranking",
                    'genus', 'species', 'infra_rank', 'infra_name',
                    'infra_rank2', 'infra_name2',
                    "vernacular", "all_vernaculars",
                    'author', 'editor', 'reference', 'comments',
                    'is_current', 'informal',
                    'added_on', 'updated_on',
                    'ogc_fid', 'md5_rowhash')
    list_filter = (
        'kingdom_id', 'rank_name',
        'is_current', 'informal', "naturalised",)
    search_fields = (
        'genus', 'species',
        'infra_rank', 'infra_name',
        'infra_rank2', 'infra_name2',
        "vernacular", "all_vernaculars",)


@admin.register(HbvVernacular)
class HbvVernacularAdmin(VersionAdmin, admin.ModelAdmin):
    """Admin for HbvVernacular."""

    save_on_top = True
    # date_hierarchy = 'updated_on'
    list_display = (
        "name_id",
        "name",
        "vernacular",
        "language",
        "lang_pref",
        "preferred",
        "source",
        "updated_by",
        'updated_on',
        'ogc_fid',
        'md5_rowhash')
    list_filter = ('language', 'lang_pref', 'preferred',)
    search_fields = ('name', 'vernacular', 'source', )


@admin.register(HbvXref)
class HbvXrefAdmin(VersionAdmin, admin.ModelAdmin):
    """Admin for HbvXref."""

    save_on_top = True
    # date_hierarchy = 'updated_on'
    list_display = (
        "xref_id",
        "old_name_id",
        "new_name_id",
        "xref_type",
        "active",
        "authorised_by",
        "authorised_on",
        "comments",
        "added_on",
        'updated_on',
        'ogc_fid',
        'md5_rowhash')
    list_filter = ('xref_type', 'active', )
    search_fields = ('old_name_id', 'new_name_id', )


@admin.register(Taxon)
class TaxonAdmin(MPTTModelAdmin, VersionAdmin):
    """Admin for Taxon."""
    list_filter = (
        'rank',
        'publication_status',
        'current',
        ('parent', TreeRelatedFieldListFilter),

    )