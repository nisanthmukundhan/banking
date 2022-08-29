from django.db import models

# Create your models here.
from django.urls import reverse


class District(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'district'
        verbose_name_plural = 'districts'

    def get_url(self):
        return reverse('finalapp:d_by_details', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Branch(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'branch'
        verbose_name_plural = 'branches'

    def __str__(self):
        return '{}'.format(self.name)


class Registerr(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    male = models.BooleanField('male', default=False)
    female = models.BooleanField('female', default=False)
    address = models.TextField(max_length=200)
    dob = models.DateField()
    acc = (('s', 'SAVING'), ('c', 'CURRENT'))
    account = models.CharField(max_length=10, choices=acc)
    mater = (('debit', 'DEBIT'), ('credit', 'CREDIT'), ('cheque', 'CHEQUEBOOK'))
    materials = models.CharField(max_length=50, choices=mater)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)
