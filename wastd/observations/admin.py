# -*- coding: utf-8 -*-
"""Admin module for wastd.observations."""
from __future__ import absolute_import, unicode_literals

# from django import forms as django_forms
import floppyforms as ff
from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from django_select2.forms import ModelSelect2Widget
from easy_select2 import select2_modelform as s2form
# from easy_select2.widgets import Select2
from fsm_admin.mixins import FSMTransitionMixin
# from wastd.observations.filters import LocationListFilter
from rest_framework.authtoken.admin import TokenAdmin
from reversion.admin import VersionAdmin
from shared.admin import CustomStateLogInline

from wastd.observations.models import (
    AnimalEncounter,
    Area,
    DispatchRecord,
    DugongMorphometricObservation,
    Encounter,
    FieldMediaAttachment,
    HatchlingMorphometricObservation,
    LineTransectEncounter,
    LoggerEncounter,
    ManagementAction,
    MediaAttachment,
    NestTagObservation,
    Survey,
    TagObservation,
    TemperatureLoggerDeployment,
    TemperatureLoggerSettings,
    TrackTallyObservation,
    TurtleDamageObservation,
    TurtleMorphometricObservation,
    TurtleNestDisturbanceObservation,
    TurtleNestDisturbanceTallyObservation,
    TurtleNestEncounter,
    TurtleNestObservation,
    PathToSea,
    TurtleHatchlingEmergenceObservation,
    TurtleHatchlingEmergenceOutlierObservation,
    LightSourceObservation
)

from shared.admin import FORMFIELD_OVERRIDES, S2ATTRS

TokenAdmin.raw_id_fields = ('user',)


class ImageThumbnailFileInput(ff.ClearableFileInput):
    """Image thumbnail admin."""

    template_name = 'floppyforms/image_thumbnail.html'


class MediaAttachmentInline(admin.TabularInline):
    """TabularInlineAdmin for MediaAttachment."""

    extra = 0
    model = MediaAttachment
    classes = ('grp-collapse grp-open',)
    widgets = {'attachment': ImageThumbnailFileInput}  # seems inactive


class TagObservationInline(admin.TabularInline):
    """TabularInlineAdmin for TagObservation."""

    extra = 0
    model = TagObservation
    classes = ('grp-collapse grp-open',)


class NestTagObservationInline(admin.StackedInline):
    """TabularInlineAdmin for NestTagObservation."""

    extra = 0
    model = NestTagObservation
    classes = ('grp-collapse grp-open',)


class TurtleMorphometricObservationInline(admin.StackedInline):
    """Admin for TurtleMorphometricObservation."""

    extra = 0
    model = TurtleMorphometricObservation
    classes = ('grp-collapse grp-open',)


class HatchlingMorphometricObservationInline(admin.TabularInline):
    """Admin for HatchlingMorphometricObservation."""

    extra = 0
    model = HatchlingMorphometricObservation
    classes = ('grp-collapse grp-open',)


class DugongMorphometricObservationInline(admin.TabularInline):
    """Admin for DugongMorphometricObservation."""

    extra = 0
    model = DugongMorphometricObservation
    classes = ('grp-collapse grp-open',)


class ManagementActionInline(admin.TabularInline):
    """TabularInlineAdmin for ManagementAction."""

    extra = 0
    model = ManagementAction
    classes = ('grp-collapse grp-open',)


class TurtleDamageObservationInline(admin.TabularInline):
    """Admin for TurtleDamageObservation."""

    extra = 0
    model = TurtleDamageObservation
    classes = ('grp-collapse grp-open',)


class TrackTallyObservationInline(admin.TabularInline):
    """Admin for TrackTallyObservation."""

    extra = 0
    model = TrackTallyObservation
    classes = ('grp-collapse grp-open',)


class TurtleNestDisturbanceTallyObservationInline(admin.TabularInline):
    """Admin for TurtleNestDisturbanceTallyObservation."""

    extra = 0
    model = TurtleNestDisturbanceTallyObservation
    classes = ('grp-collapse grp-open',)


class TurtleNestObservationInline(admin.StackedInline):
    """Admin for TurtleNestObservation."""

    extra = 0
    model = TurtleNestObservation
    classes = ('grp-collapse grp-open',)


class TurtleNestDisturbanceObservationInline(admin.TabularInline):
    """Admin for TurtleNestDisturbanceObservation."""

    extra = 0
    model = TurtleNestDisturbanceObservation
    classes = ('grp-collapse grp-open',)


class TurtleHatchlingEmergenceObservationInline(admin.StackedInline):
    """Admin for TurtleHatchlingEmergenceObservation."""

    extra = 0
    model = TurtleHatchlingEmergenceObservation
    classes = ('grp-collapse grp-open',)


class TurtleHatchlingEmergenceOutlierObservationInline(admin.TabularInline):
    """Admin for TurtleHatchlingEmergenceOutlierObservation."""

    extra = 0
    model = TurtleHatchlingEmergenceOutlierObservation
    classes = ('grp-collapse grp-open',)


class LightSourceObservationObservationInline(admin.TabularInline):
    """Admin for LightSourceObservation."""

    extra = 0
    model = LightSourceObservation
    classes = ('grp-collapse grp-open',)


class TemperatureLoggerSettingsInline(admin.TabularInline):
    """Admin for TemperatureLoggerSettings."""

    extra = 0
    model = TemperatureLoggerSettings
    classes = ('grp-collapse grp-open',)


class DispatchRecordInline(admin.TabularInline):
    """Admin for DispatchRecord."""

    extra = 0
    model = DispatchRecord
    classes = ('grp-collapse grp-open',)


class TemperatureLoggerDeploymentInline(admin.TabularInline):
    """Admin for TemperatureLoggerDeployment."""

    extra = 0
    model = TemperatureLoggerDeployment
    classes = ('grp-collapse grp-open',)


class ObservationAdminMixin(VersionAdmin, admin.ModelAdmin):
    """Admin mixin for Observation models."""

    save_on_top = True
    date_hierarchy = 'encounter__when'
    LIST_FIRST = (
        'pk',
        'area',
        'site',
        'latitude',
        'longitude',
        'date',
    )
    LIST_LAST = (
        'encounter_link',
        'encounter_status',
    )
    LIST_FILTER = (
        'encounter__area',
        'encounter__site',
        'encounter__status',
        'encounter__encounter_type',
    )
    search_fields = ('comments', )
    readonly_fields = ('encounter', )

    area = forms.ChoiceField(
        widget=ModelSelect2Widget(
            model=Area,
            search_fields=["name__icontains", ]
        )
    )
    site = forms.ChoiceField(
        widget=ModelSelect2Widget(
            model=Area,
            search_fields=["name__icontains", ]
        )
    )

    def area(self, obj):
        """Make data source readable."""
        return obj.encounter.area
    area.short_description = 'Area'

    def site(self, obj):
        """Make data source readable."""
        return obj.encounter.site
    site.short_description = 'Site'

    def status(self, obj):
        """Make health status human readable."""
        return obj.encounter.get_status_display()
    status.short_description = 'Status'

    def latitude(self, obj):
        """Make data source readable."""
        return obj.encounter.latitude
    latitude.short_description = 'Latitude'

    def longitude(self, obj):
        """Make data source readable."""
        return obj.encounter.longitude
    longitude.short_description = 'Longitude'

    def date(self, obj):
        """Make data source readable."""
        return obj.encounter.when
    date.short_description = 'Date'

    def encounter_link(self, obj):
        """A link to the encounter."""
        return mark_safe(
            '<a href="{0}">{1}</a>'.format(obj.encounter.absolute_admin_url,
                                           obj.encounter.__str__()))
    encounter_link.short_description = 'Encounter'
    encounter_link.allow_tags = True

    def encounter_status(self, obj):
        """A link to the encounter."""
        return obj.encounter.get_status_display()
    encounter_status.short_description = 'QA status'


@admin.register(ManagementAction)
class ManagementActionAdmin(ObservationAdminMixin):
    """Admin for ManagementAction."""

    # save_on_top = True
    # date_hierarchy = 'encounter__when'
    list_display = ObservationAdminMixin.LIST_FIRST + (
        'management_actions',
        'comments',
    ) + ObservationAdminMixin.LIST_LAST

    list_filter = ObservationAdminMixin.LIST_FILTER + ()
    search_fields = ('management_actions', 'comments', )

    def get_queryset(self, request):
        return super(
            ManagementActionAdmin, self
        ).get_queryset(
            request
        ).prefetch_related(
            'encounter',
            'encounter__reporter',
            'encounter__observer',
            'encounter__area',
            'encounter__site',
        )


@admin.register(MediaAttachment)
class MediaAttachmentAdmin(ObservationAdminMixin):
    """Admin for MediaAttachment."""

    # save_on_top = True
    # date_hierarchy = 'encounter__when'
    list_display = ObservationAdminMixin.LIST_FIRST + (
        'media_type',
        'title',
        'thumbnail',
    ) + ObservationAdminMixin.LIST_LAST

    list_filter = ObservationAdminMixin.LIST_FILTER + (
        'media_type',
    )
    search_fields = ('title', )
    # readonly_fields = ('thumbnail',)

    def get_queryset(self, request):
        return super(
            MediaAttachmentAdmin, self
        ).get_queryset(
            request
        ).prefetch_related(
            'encounter',
            'encounter__reporter',
            'encounter__observer',
            'encounter__area',
            'encounter__site',
        )

    def thumbnail(self, obj):
        return obj.thumbnail

    thumbnail.short_description = 'Preview'
    thumbnail.allow_tags = True


@admin.register(TurtleMorphometricObservation)
class TurtleMorphometricObservationAdmin(ObservationAdminMixin):
    """Admin for TurtleMorphometricObservation."""

    list_display = ObservationAdminMixin.LIST_FIRST + (
        "curved_carapace_length_mm",
        # "curved_carapace_length_accuracy",
        "curved_carapace_length_min_mm",
        # "curved_carapace_length_min_accuracy",
        "straight_carapace_length_mm",
        # "straight_carapace_length_accuracy",
        "curved_carapace_width_mm",
        # "curved_carapace_width_accuracy",
        "tail_length_carapace_mm",
        # "tail_length_carapace_accuracy",
        "tail_length_vent_mm",
        # "tail_length_vent_accuracy",
        "tail_length_plastron_mm",
        # "tail_length_plastron_accuracy",
        "maximum_head_width_mm",
        # "maximum_head_width_accuracy",
        "maximum_head_length_mm",
        # "maximum_head_length_accuracy",
        "body_depth_mm",
        # "body_depth_accuracy",
        "body_weight_g",
        # "body_weight_accuracy",
        "handler",
        "recorder",
    ) + ObservationAdminMixin.LIST_LAST
    list_filter = ObservationAdminMixin.LIST_FILTER + \
        ()
    search_fields = ()

    handler = forms.ChoiceField(
        widget=ModelSelect2Widget(
            model=get_user_model(),
            search_fields=[
                "username__icontains",
                "name__icontains",
                "role__icontains",
                "email__icontains"]
        )
    )
    recorder = forms.ChoiceField(
        widget=ModelSelect2Widget(
            model=get_user_model(),
            search_fields=[
                "username__icontains",
                "name__icontains",
                "role__icontains",
                "email__icontains"]
        )
    )

    def get_queryset(self, request):
        return super(
            TurtleMorphometricObservationAdmin, self
        ).get_queryset(
            request
        ).prefetch_related(
            'encounter',
            'handler',
            'recorder',
            'encounter__reporter',
            'encounter__observer',
            'encounter__area',
            'encounter__site',
        )


@admin.register(TagObservation)
class TagObservationAdmin(ObservationAdminMixin):
    """Admin for TagObservation."""

    list_display = ObservationAdminMixin.LIST_FIRST + (
        'type_display', 'name', 'tag_location_display',
    ) + ObservationAdminMixin.LIST_LAST
    list_filter = ObservationAdminMixin.LIST_FILTER + \
        ('tag_type', 'tag_location',)
    search_fields = ('name', 'comments')
    # autocomplete_lookup_fields = {'fk': ['handler', 'recorder', ], }
    handler = forms.ChoiceField(
        widget=ModelSelect2Widget(
            model=get_user_model(),
            search_fields=[
                "username__icontains",
                "name__icontains",
                "role__icontains",
                "email__icontains"]
        )
    )
    recorder = forms.ChoiceField(
        widget=ModelSelect2Widget(
            model=get_user_model(),
            search_fields=[
                "username__icontains",
                "name__icontains",
                "role__icontains",
                "email__icontains"]
        )
    )

    def type_display(self, obj):
        """Make tag type human readable."""
        return obj.get_tag_type_display()
    type_display.short_description = 'Tag Type'

    def tag_location_display(self, obj):
        """Make tag side human readable."""
        return obj.get_tag_location_display()
    tag_location_display.short_description = 'Tag Location'

    def animal_name(self, obj):
        """Animal name."""
        return obj.encounter.name
    animal_name.short_description = 'Animal Name'


@admin.register(TurtleDamageObservation)
class TurtleDamageObservationAdmin(ObservationAdminMixin):
    """Admin for TurtleDamageObservation."""

    # save_on_top = True
    # date_hierarchy = 'encounter__when'
    list_display = ObservationAdminMixin.LIST_FIRST + (
        'body_part',
        'damage_type',
        'damage_age',
        'description',
    ) + ObservationAdminMixin.LIST_LAST

    list_filter = ObservationAdminMixin.LIST_FILTER + (
        'body_part',
        'damage_type',
        'damage_age',
    )

    def get_queryset(self, request):
        return super(
            TurtleDamageObservationAdmin, self
        ).get_queryset(
            request
        ).prefetch_related(
            'encounter',
            'encounter__reporter',
            'encounter__observer',
            'encounter__area',
            'encounter__site',
        )



@admin.register(TurtleNestDisturbanceObservation)
class TurtleNestDisturbanceObservationAdmin(ObservationAdminMixin):
    """Admin for TurtleNestDisturbanceObservation."""

    # save_on_top = True
    # date_hierarchy = 'encounter__when'
    list_display = ObservationAdminMixin.LIST_FIRST + (
        'disturbance_cause',
        'disturbance_cause_confidence',
        'disturbance_severity',
        'comments',
    ) + ObservationAdminMixin.LIST_LAST

    list_filter = ObservationAdminMixin.LIST_FILTER + (
        'disturbance_cause_confidence',
        'disturbance_severity',
    )

    def get_queryset(self, request):
        return super(
            TurtleNestDisturbanceObservationAdmin, self
        ).get_queryset(
            request
        ).prefetch_related(
            'encounter',
            'encounter__reporter',
            'encounter__observer',
            'encounter__area',
            'encounter__site',
        )


@admin.register(TurtleNestObservation)
class TurtleNestObservationAdmin(ObservationAdminMixin):
    """Admin for TurtleNestObservation."""

    list_display = ObservationAdminMixin.LIST_FIRST + (
        'nest_position', 'eggs_laid', 'egg_count',
        'hatching_success', 'emergence_success',
        'no_egg_shells', 'no_live_hatchlings_neck_of_nest', 'no_live_hatchlings',
        'no_dead_hatchlings', 'no_undeveloped_eggs',
        'no_unhatched_eggs', 'no_unhatched_term', 'no_depredated_eggs',
        'nest_depth_top', 'nest_depth_bottom',
    ) + ObservationAdminMixin.LIST_LAST
    list_filter = ObservationAdminMixin.LIST_FILTER + \
        ('nest_position', 'eggs_laid',)

    def get_queryset(self, request):
        return super(
            TurtleNestObservationAdmin, self
        ).get_queryset(
            request
        ).prefetch_related(
            'encounter',
            'encounter__reporter',
            'encounter__observer',
            'encounter__area',
            'encounter__site',
        )


@admin.register(NestTagObservation)
class NestTagObservationAdmin(ObservationAdminMixin):
    """Admin for NestTagObservation."""

    list_display = ObservationAdminMixin.LIST_FIRST + (
        'tag_name', 'flipper_tag_id', 'date_nest_laid', 'tag_label',
    ) + ObservationAdminMixin.LIST_LAST
    list_filter = ObservationAdminMixin.LIST_FILTER + \
        ('flipper_tag_id', 'tag_label',)
    search_fields = ('flipper_tag_id', 'date_nest_laid',
                     'tag_label', 'comments')

    def tag_name(self, obj):
        """Nest tag name."""
        return obj.name
    tag_name.short_description = 'Nest Tag ID'

    def get_queryset(self, request):
        return super(
            NestTagObservationAdmin, self
        ).get_queryset(
            request
        ).prefetch_related(
            'encounter',
            'encounter__reporter',
            'encounter__observer',
            'encounter__area',
            'encounter__site',
        )


@admin.register(HatchlingMorphometricObservation)
class HatchlingMorphometricObservationAdmin(ObservationAdminMixin):
    """Admin for HatchlingMorphometricObservation."""

    list_display = ObservationAdminMixin.LIST_FIRST + (
        "straight_carapace_length_mm",
        "straight_carapace_width_mm",
        "body_weight_g"
    ) + ObservationAdminMixin.LIST_LAST
    list_filter = ObservationAdminMixin.LIST_FILTER + \
        ()
    search_fields = ()

    def get_queryset(self, request):
        return super(
            HatchlingMorphometricObservationAdmin, self
        ).get_queryset(
            request
        ).prefetch_related(
            'encounter',
            'encounter__reporter',
            'encounter__observer',
            'encounter__area',
            'encounter__site',
        )


@admin.register(TurtleHatchlingEmergenceObservation)
class TurtleHatchlingEmergenceObservationAdmin(ObservationAdminMixin):
    """Admin for TurtleHatchlingEmergenceObservation."""

    list_display = ObservationAdminMixin.LIST_FIRST + (
        "bearing_to_water_degrees",
        "bearing_leftmost_track_degrees",
        "bearing_rightmost_track_degrees",
        "no_tracks_main_group",
        "no_tracks_main_group_min",
        "no_tracks_main_group_max",
        "outlier_tracks_present",
        "path_to_sea_comments",
        "hatchling_emergence_time_known",
        "cloud_cover_at_emergence_known",
        "light_sources_present",
        "hatchling_emergence_time",
        "hatchling_emergence_time_accuracy",
        "cloud_cover_at_emergence",
    ) + ObservationAdminMixin.LIST_LAST
    list_filter = ObservationAdminMixin.LIST_FILTER + \
        ()
    search_fields = ()

    def get_queryset(self, request):
        return super(
            TurtleHatchlingEmergenceObservationAdmin, self
        ).get_queryset(
            request
        ).prefetch_related(
            'encounter',
            'encounter__reporter',
            'encounter__observer',
            'encounter__area',
            'encounter__site',
        )


@admin.register(TurtleHatchlingEmergenceOutlierObservation)
class TurtleHatchlingEmergenceOutlierObservationAdmin(ObservationAdminMixin):
    """Admin for TurtleHatchlingEmergenceOutlierObservation."""

    list_display = ObservationAdminMixin.LIST_FIRST + (
        "bearing_outlier_track_degrees",
        "outlier_group_size",
        "outlier_track_comment",
    ) + ObservationAdminMixin.LIST_LAST
    list_filter = ObservationAdminMixin.LIST_FILTER + \
        ()
    search_fields = ()

    def get_queryset(self, request):
        return super(
            TurtleHatchlingEmergenceOutlierObservationAdmin, self
        ).get_queryset(
            request
        ).prefetch_related(
            'encounter',
            'encounter__reporter',
            'encounter__observer',
            'encounter__area',
            'encounter__site',
        )


@admin.register(LightSourceObservation)
class LightSourceObservationAdmin(ObservationAdminMixin):
    """Admin for LightSourceObservation."""

    list_display = ObservationAdminMixin.LIST_FIRST + (
        "bearing_light_degrees",
        "light_source_type",
        "light_source_description",
    ) + ObservationAdminMixin.LIST_LAST
    list_filter = ObservationAdminMixin.LIST_FILTER + \
        ()
    search_fields = ()

    def get_queryset(self, request):
        return super(
            LightSourceObservationAdmin, self
        ).get_queryset(
            request
        ).prefetch_related(
            'encounter',
            'encounter__reporter',
            'encounter__observer',
            'encounter__area',
            'encounter__site',
        )


@admin.register(TrackTallyObservation)
class TrackTallyObservationAdmin(ObservationAdminMixin):
    """Admin for TrackTallyObservation."""

    list_display = ObservationAdminMixin.LIST_FIRST + (
        "species",
        "nest_age",
        "nest_type",
        "tally",
    ) + ObservationAdminMixin.LIST_LAST
    list_filter = ObservationAdminMixin.LIST_FILTER + \
        ("species",
         "nest_age",
         "nest_type",)
    search_fields = ()

    def get_queryset(self, request):
        return super(
            TrackTallyObservationAdmin, self
        ).get_queryset(
            request
        ).prefetch_related(
            'encounter',
            'encounter__reporter',
            'encounter__observer',
            'encounter__area',
            'encounter__site',
        )


@admin.register(TurtleNestDisturbanceTallyObservation)
class TurtleNestDisturbanceTallyObservationAdmin(ObservationAdminMixin):
    """Admin for TurtleNestDisturbanceTallyObservation."""

    list_display = ObservationAdminMixin.LIST_FIRST + (
        "species",
        "disturbance_cause",
        "no_nests_disturbed",
        "no_tracks_encountered",
        "comments"
    ) + ObservationAdminMixin.LIST_LAST
    list_filter = ObservationAdminMixin.LIST_FILTER + \
        ("species",
         "disturbance_cause",)
    search_fields = ("comments", )

    def get_queryset(self, request):
        return super(
            TurtleNestDisturbanceTallyObservationAdmin, self
        ).get_queryset(
            request
        ).prefetch_related(
            'encounter',
            'encounter__reporter',
            'encounter__observer',
            'encounter__area',
            'encounter__site',
        )


class FieldMediaAttachmentInline(admin.TabularInline):
    """TabularInlineAdmin for FieldMediaAttachment."""

    extra = 0
    model = FieldMediaAttachment
    classes = ('grp-collapse grp-open',)
    widgets = {'attachment': ImageThumbnailFileInput}  # seems inactive


@admin.register(Survey)
class SurveyAdmin(FSMTransitionMixin, VersionAdmin, admin.ModelAdmin):
    """Survey Admin."""

    # model = Survey
    # change list
    date_hierarchy = 'start_time'
    list_select_related = ('site', 'reporter', )
    list_display = (
        '__str__',
        'source',
        'device_id',
        'end_device_id',
        'site',
        'start_time',
        'end_time',
        'reporter',
        'start_comments',
        'end_comments',
        'status',
        'production',
    )
    list_filter = ('device_id', 'site', 'reporter', 'status', 'production')
    search_fields = (
        'site__name',
        'start_comments',
        'end_comments',
        'reporter__name',
        'reporter__username'
    )

    # change view
    form = s2form(Survey, attrs=S2ATTRS)
    formfield_overrides = FORMFIELD_OVERRIDES
    fsm_field = ['status', ]
    fieldsets = (
        (_('Device'),
            {'classes': ('grp-collapse', 'grp-open', 'wide', 'extrapretty'),
             'fields': ('source', 'source_id', 'device_id',
                        'end_source_id', 'end_device_id', 'production',)}),
        (_('Location'),
            {'classes': ('grp-collapse', 'grp-open', 'wide', 'extrapretty'),
             'fields': ('transect', 'start_location', 'end_location', 'site',)}),
        (_('Time'),
            {'classes': ('grp-collapse', 'grp-open', 'wide', 'extrapretty'),
             'fields': ('start_time', 'end_time',)}),
        (_('Team'),
            {'classes': ('grp-collapse', 'grp-open', 'wide', 'extrapretty'),
             'fields': ('start_comments', 'end_comments', 'reporter', 'team',
                        'start_photo', 'end_photo',
                        )}),
    )
    inlines = [CustomStateLogInline, ]


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    """Area admin."""

    list_display = ("area_type", "name", "northern_extent", "centroid", )
    list_filter = ("area_type", )
    search_fields = ("name__icontains", )
    form = s2form(Area, attrs=S2ATTRS)
    formfield_overrides = FORMFIELD_OVERRIDES


@admin.register(Encounter)
class EncounterAdmin(FSMTransitionMixin, VersionAdmin):
    """Admin for Encounter with inlines for all Observations.

    This admin can be extended by other Encounter Admin classes.
    """

    # -------------------------------------------------------------------------
    # Change list
    change_list_filter_template = "admin/filter_listing.html"

    date_hierarchy = 'when'
    # Filters for change_list
    list_filter = (
        'area', 'site', 'status',
        # 'observer', 'reporter',

        'location_accuracy',
        'encounter_type', 'source')  # 'survey',

    # Columns for change_list, allow re-use and inserting fields
    FIRST_COLS = ('when', 'area', 'site', 'latitude', 'longitude',
                  'location_accuracy', 'location_accuracy_m', 'name')
    LAST_COLS = ('observer', 'reporter', 'source_display', 'source_id',
                 'status', 'encounter_type')  # 'survey',
    list_display = FIRST_COLS + LAST_COLS
    # Layout: save buttons also on top - overridden by Grapelli admin skin
    # save_on_top = True

    # Change_list fulltext search fields
    search_fields = ('observer__name', 'observer__username', 'name',
                     'reporter__name', 'reporter__username', 'source_id',)

    # Performance
    # https://docs.djangoproject.com/en/1.11/ref/contrib/admin/
    # #django.contrib.admin.ModelAdmin.list_select_related
    list_select_related = ('area', 'site', 'survey', 'observer', 'reporter', )

    # -------------------------------------------------------------------------
    # Change form
    # select2 widgets for searchable dropdowns
    form = s2form(Encounter, attrs=S2ATTRS)
    formfield_overrides = FORMFIELD_OVERRIDES
    autocomplete_fields = ['area', 'site', 'survey', 'observer', 'reporter', ]
    # observer = forms.ChoiceField(
    #     widget=ModelSelect2Widget(
    #         model=get_user_model(),
    #         search_fields=[
    #             "username__icontains",
    #             "name__icontains",
    #             "role__icontains",
    #             "email__icontains"]
    #     )
    # )
    # reporter = forms.ChoiceField(
    #     widget=ModelSelect2Widget(
    #         model=get_user_model(),
    #         search_fields=[
    #             "username__icontains",
    #             "name__icontains",
    #             "role__icontains",
    #             "email__icontains"]
    #     )
    # )
    # area = forms.ChoiceField(
    #     widget=ModelSelect2Widget(
    #         model=Area,
    #         search_fields=["name__icontains", ]
    #     )
    # )
    # site = forms.ChoiceField(
    #     widget=ModelSelect2Widget(
    #         model=Area,
    #         search_fields=["name__icontains", ]
    #     )
    # )
    # survey = forms.ChoiceField(
    #     widget=ModelSelect2Widget(
    #         model=Survey,
    #         search_fields=["site_name__icontains", "reporter__name__icontains", ]
    #     )
    # )

    # Django-fsm transitions config
    fsm_field = ['status', ]

    # Change_view form layout
    fieldsets = (
        ('Encounter',
            {
                'classes': ('grp-collapse', 'grp-open', 'wide', 'extrapretty'),
                'fields': (
                    'area', 'site', 'survey',
                    'where',
                    'location_accuracy',
                    'location_accuracy_m',
                    'when',
                    'observer', 'reporter',
                    'source', 'source_id',
                )
            }
         ),
    )

    # Change_view inlines
    inlines = [
        MediaAttachmentInline,
        TagObservationInline,
        TurtleDamageObservationInline,
        TurtleMorphometricObservationInline,
        TrackTallyObservationInline,
        TurtleNestDisturbanceTallyObservationInline,
        ManagementActionInline,
        NestTagObservationInline,
        TurtleNestObservationInline,
        TurtleNestDisturbanceObservationInline,
        HatchlingMorphometricObservationInline,
        TurtleHatchlingEmergenceObservationInline,
        TurtleHatchlingEmergenceOutlierObservationInline,
        LightSourceObservationObservationInline,
        CustomStateLogInline
    ]

    def get_queryset(self, request):
        return super(
            EncounterAdmin, self
        ).get_queryset(
            request
        ).prefetch_related(
            'observer', 'reporter', 'area', 'site',
        )

    def source_display(self, obj):
        """Make data source readable."""
        return obj.get_source_display()
    source_display.short_description = 'Data Source'

    def latitude(self, obj):
        """Make data source readable."""
        return obj.latitude
    latitude.short_description = 'Latitude'

    def longitude(self, obj):
        """Make data source readable."""
        return obj.longitude
    longitude.short_description = 'Longitude'

    def encounter_type_display(self, obj):
        """Make encounter type readable."""
        return obj.get_encounter_type_display()
    encounter_type_display.short_description = 'Encounter Type'


@admin.register(AnimalEncounter)
class AnimalEncounterAdmin(EncounterAdmin):
    """Admin for AnimalEncounter."""

    form = s2form(AnimalEncounter, attrs=S2ATTRS)
    list_display = EncounterAdmin.FIRST_COLS + (
        'taxon', 'species', 'health_display',
        'cause_of_death', 'cause_of_death_confidence',
        'maturity_display', 'sex_display', 'behaviour',
        'habitat_display',
        'nesting_event',
        'checked_for_injuries',
        'scanned_for_pit_tags',
        'checked_for_flipper_tags',
    ) + EncounterAdmin.LAST_COLS
    list_select_related = ('area', 'site', 'survey', )
    list_filter = EncounterAdmin.list_filter + (
        'taxon', 'species',
        'health', 'cause_of_death', 'cause_of_death_confidence',
        'maturity', 'sex', 'habitat',
        'nesting_event',
        'checked_for_injuries',
        'scanned_for_pit_tags',
        'checked_for_flipper_tags', )
    fieldsets = EncounterAdmin.fieldsets + (
        ('Animal',
         {'classes': ('grp-collapse', 'grp-open', 'wide', 'extrapretty'),
          'fields': ('taxon', 'species', 'maturity', 'sex',
                     'activity', 'behaviour', 'habitat',
                     'health', 'cause_of_death', 'cause_of_death_confidence',
                     'nesting_event',
                     'checked_for_injuries',
                     'scanned_for_pit_tags',
                     'checked_for_flipper_tags',)}), )
    inlines = [
        MediaAttachmentInline,
        TagObservationInline,
        TurtleDamageObservationInline,
        TurtleMorphometricObservationInline,
        DugongMorphometricObservationInline,
        TurtleNestObservationInline,
        NestTagObservationInline,
        ManagementActionInline,
        CustomStateLogInline
    ]

    def get_queryset(self, request):
        return super(
            AnimalEncounterAdmin, self
        ).get_queryset(
            request
        ).prefetch_related(
            'observer', 'reporter', 'area', 'site',
        )

    def health_display(self, obj):
        """Make health status human readable."""
        return obj.get_health_display()
    health_display.short_description = 'Health'

    def maturity_display(self, obj):
        """Make maturity human readable."""
        return obj.get_maturity_display()
    maturity_display.short_description = 'Maturity'

    def sex_display(self, obj):
        """Make sex human readable."""
        return obj.get_sex_display()
    sex_display.short_description = 'Sex'

    def status_display(self, obj):
        """Make QA status human readable."""
        return obj.get_status_display()
    status_display.short_description = 'QA Status'

    def habitat_display(self, obj):
        """Make habitat human readable."""
        return obj.get_habitat_display()
    habitat_display.short_description = 'Habitat'


@admin.register(TurtleNestEncounter)
class TurtleNestEncounterAdmin(EncounterAdmin):
    """Admin for TurtleNestEncounter."""

    form = s2form(TurtleNestEncounter, attrs=S2ATTRS)
    list_display = EncounterAdmin.FIRST_COLS + (
        'age_display', 'type_display', 'species',
        'habitat_display', 'disturbance', 'comments'
    ) + EncounterAdmin.LAST_COLS
    list_select_related = True
    list_filter = EncounterAdmin.list_filter + (
        'nest_age', 'nest_type', 'species', 'habitat',
        'disturbance', 'nest_tagged', 'logger_found',
        'eggs_counted', 'hatchlings_measured', 'fan_angles_measured',
    )
    fieldsets = EncounterAdmin.fieldsets + (
        ('Nest',
            {
                'classes': ('grp-collapse', 'grp-open', 'wide', 'extrapretty'),
                'fields': (
                    'nest_age', 'nest_type', 'species', 'habitat',
                    'disturbance', 'nest_tagged', 'logger_found', 'eggs_counted',
                    'hatchlings_measured', 'fan_angles_measured', 'comments'
                )
            }
         ),
    )
    inlines = [
        MediaAttachmentInline,
        NestTagObservationInline,
        TurtleNestObservationInline,
        TurtleNestDisturbanceObservationInline,
        HatchlingMorphometricObservationInline,
        TurtleHatchlingEmergenceObservationInline,
        TurtleHatchlingEmergenceOutlierObservationInline,
        LightSourceObservationObservationInline,
        CustomStateLogInline
    ]

    def get_queryset(self, request):
        return super(
            TurtleNestEncounterAdmin, self
        ).get_queryset(
            request
        ).prefetch_related(
            'observer', 'reporter', 'area', 'site'
        )

    def habitat_display(self, obj):
        """Make habitat human readable."""
        return obj.get_habitat_display()
    habitat_display.short_description = 'Habitat'

    def age_display(self, obj):
        """Make nest age human readable."""
        return obj.get_nest_age_display()
    age_display.short_description = 'Nest age'

    def type_display(self, obj):
        """Make nest type human readable."""
        return obj.get_nest_type_display()
    type_display.short_description = 'Nest type'


@admin.register(LineTransectEncounter)
class LineTransectEncounterAdmin(EncounterAdmin):
    """Admin for LineTransectEncounter."""

    form = s2form(LineTransectEncounter, attrs=S2ATTRS)
    list_display = EncounterAdmin.FIRST_COLS + (
        'transect',
    ) + EncounterAdmin.LAST_COLS
    list_select_related = ('area', 'site', 'survey', )
    # list_filter = EncounterAdmin.list_filter + ()
    fieldsets = EncounterAdmin.fieldsets + (
        ('Location',
            {
                'classes': ('grp-collapse', 'grp-open', 'wide', 'extrapretty'),
                'fields': ('transect', )
            }), )
    inlines = [
        TrackTallyObservationInline,
        TurtleNestDisturbanceTallyObservationInline,
        CustomStateLogInline
    ]

    def get_queryset(self, request):
        return super(
            LineTransectEncounterAdmin, self
        ).get_queryset(
            request
        ).prefetch_related(
            'observer', 'reporter', 'area', 'site',
        )


@admin.register(LoggerEncounter)
class LoggerEncounterAdmin(EncounterAdmin):
    """Admin for LoggerEncounter."""

    form = s2form(LoggerEncounter, attrs=S2ATTRS)
    list_display = EncounterAdmin.FIRST_COLS + (
        'logger_type_display', 'deployment_status_display',
        'logger_id', 'comments',
    ) + EncounterAdmin.LAST_COLS
    list_select_related = ('area', 'site', 'survey', )
    list_filter = EncounterAdmin.list_filter + \
        ('logger_type', 'deployment_status',)
    search_fields = ('logger_id', 'source_id')
    fieldsets = EncounterAdmin.fieldsets + (
        ('Logger',
            {
                'classes': ('grp-collapse', 'grp-open', 'wide', 'extrapretty'),
                'fields': (
                    'logger_type', 'deployment_status', 'logger_id', 'comments',)
            }), )
    inlines = [
        MediaAttachmentInline,
        TagObservationInline,
        NestTagObservationInline,
        TemperatureLoggerSettingsInline,
        DispatchRecordInline,
        TemperatureLoggerDeploymentInline,
        CustomStateLogInline
    ]

    def get_queryset(self, request):
        return super(
            LoggerEncounterAdmin, self
        ).get_queryset(
            request
        ).prefetch_related(
            'observer', 'reporter', 'area', 'site',
        )

    def logger_type_display(self, obj):
        """Make habitat human readable."""
        return obj.get_logger_type_display()
    logger_type_display.short_description = 'Logger Type'

    def deployment_status_display(self, obj):
        """Make habitat human readable."""
        return obj.get_deployment_status_display()
    deployment_status_display.short_description = 'Deployment Status'
