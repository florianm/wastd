"""Taxonomy filters."""
# from django.contrib.auth.models import User
import django_filters
from django_filters.filters import BooleanFilter
from django_filters.widgets import BooleanWidget
from django.db import models
# from django import forms
from .models import Taxon, Community


class TaxonFilter(django_filters.FilterSet):
    """Filter for Taxon."""

    current = BooleanFilter(widget=BooleanWidget())

    class Meta:
        """Class opts."""

        model = Taxon
        fields = ['taxonomic_name', 'vernacular_names', 'rank', 'current', 'publication_status']
        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {'lookup_expr': 'icontains', },
            },
            models.TextField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {'lookup_expr': 'icontains', },
            },
            # models.BooleanField: {
            #     'filter_class': django_filters.BooleanFilter,
            #     'extra': lambda f: {'widget': forms.CheckboxInput,},
            # },
        }


class CommunityFilter(django_filters.FilterSet):
    """Filter for Community."""

    class Meta:
        """Class opts."""

        model = Community
        fields = ['code', 'name', 'description', ]
        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {'lookup_expr': 'icontains', },
            },
            models.TextField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {'lookup_expr': 'icontains', },
            },
            # models.BooleanField: {
            #     'filter_class': django_filters.BooleanFilter,
            #     'extra': lambda f: {'widget': forms.CheckboxInput,},
            # },
        }
