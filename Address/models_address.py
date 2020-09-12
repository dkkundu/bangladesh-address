from django.db import models
from django.utils.translation import gettext_lazy as _

import datetime
from django.utils import timezone



class Division(models.Model):
    """
    Future proofed the division model.
    """
    division = models.CharField(
        unique=True, max_length=50, blank=False, null=True)
    division_code = models.CharField(max_length=10, blank=False, null=True)
    division_bangla = models.CharField(
        max_length=50, blank=True, null=True, help_text='বিভাগ')
    created_at = models.DateTimeField(
        _('Created At'), auto_now_add=True, blank=False, null=True)
    updated_at = models.DateTimeField(
        _('Updated At'), auto_now=True, blank=False, null=True)
    is_active = models.BooleanField(
        _('Is Division Active?'), default=True, blank=False, null=True)

    class Meta:
        ordering = ['division']

    def __str__(self):
        return self.division


class District(models.Model):
    """
    Future proofed the district model.
    """
    district = models.CharField(
        unique=True, max_length=50, blank=False, null=True)
    district_code = models.CharField(max_length=10, blank=False, null=True)
    district_bangla = models.CharField(
        max_length=50, blank=True, null=True, help_text='জেলা')
    division = models.ForeignKey(
        Division, on_delete=models.CASCADE, blank=False, null=True)
    created_at = models.DateTimeField(
        _('Created At'), auto_now_add=True, blank=False, null=True)
    updated_at = models.DateTimeField(
        _('Updated At'), auto_now=True, blank=False, null=True)
    is_active = models.BooleanField(
        _('Is District Active?'), default=True, blank=False, null=True)

    class Meta:
        ordering = ['district']

    def __str__(self):
        return self.district


class Upazila(models.Model):
    """
    Future proofed the upazila model.
    """
    upazila = models.CharField(
        unique=True, max_length=50, blank=False, null=True)
    upazila_code = models.CharField(max_length=10, blank=False, null=True)
    upazila_bangla = models.CharField(
        max_length=50, blank=True, null=True, help_text='উপজেলা')
    district = models.ForeignKey(
    District, on_delete=models.CASCADE,
        blank=False, null=True)
    created_at = models.DateTimeField(
        _('Created At'), auto_now_add=True, blank=False, null=True)
    updated_at = models.DateTimeField(
        _('Updated At'), auto_now=True, blank=False, null=True)
    is_active = models.BooleanField(
        _('Is Upazila Active?'), default=True, blank=False, null=True)

    class Meta:
        ordering = ['upazila']

    def __str__(self):
        return self.upazila


class Union(models.Model):
    """
    Future proofed the Union model.
    """
    union = models.CharField(
        unique=False, max_length=50, blank=False, null=True)
    union_code = models.CharField(max_length=10, blank=False, null=True)
    union_bangla = models.CharField(
        max_length=50, blank=True, null=True, help_text='ইউনিয়ন')
    upazila = models.ForeignKey(
        Upazila, on_delete=models.CASCADE, blank=False,
    null=True)
    created_at = models.DateTimeField(
        _('Created At'), auto_now_add=True, blank=False, null=True)
    updated_at = models.DateTimeField(
        _('Updated At'), auto_now=True, blank=False, null=True)
    is_active = models.BooleanField(
        _('Is Union Active?'), default=True, blank=False, null=True)

    class Meta:
        ordering = ['union']

    def __str__(self):
        return self.union


class PostOffice(models.Model):
    """
    Future proofed the Post Office model.
    """
    postoffice = models.CharField(
        unique=True, max_length=50, blank=False, null=True)
    postoffice_code = models.CharField(max_length=10, blank=False, null=True)
    postoffice_bangla = models.CharField(
        max_length=50, blank=True, null=True, help_text='পোস্ট অফিস')
    upazila = models.ForeignKey(
    Upazila, on_delete=models.CASCADE, blank=False, null=True)
    created_at = models.DateTimeField(
        _('Created At'), auto_now_add=True, blank=False, null=True)
    updated_at = models.DateTimeField(
        _('Updated At'), auto_now=True, blank=False, null=True)
    is_active = models.BooleanField(
        _('Is PostOffice Active?'), default=True, blank=False, null=True)

    class Meta:
        ordering = ['postoffice']

    def __str__(self):
        return self.postoffice

class Village(models.Model):
    """
    Future proofed the Village model.
    """
    village_name = models.CharField(max_length=50, blank=False, null=True)
    village_code = models.CharField(max_length=10, blank=False, null=True)
    union = models.ForeignKey(
        Union, on_delete=models.CASCADE, blank=False, null=True)
    created_at = models.DateTimeField(
        _('Created At'), auto_now_add=True, blank=False, null=True)
    updated_at = models.DateTimeField(
        _('Updated At'), auto_now=True, blank=False, null=True)
    is_active = models.BooleanField(
        _('Is Village Active?'), default=True, blank=False, null=True)

    class Meta:
        ordering = ['village_name']

    def __str__(self):
        return self.village_name