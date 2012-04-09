from django.db import models
from django.utils.translation import ugettext_lazy as _


CONTINENTS = (
    ('AF', _('Africa')),
    ('NA', _('North America')),
    ('EU',  _('Europe')),
    ('AS', _('Asia')),
    ('OC',  _('Oceania')),
    ('SA', _('South America')),
    ('AN', _('Antarctica'))
)


class Country(models.Model):
    """
    International Organization for Standardization (ISO) 3166-1 Country list    
    """
    iso2_code = models.CharField(_('ISO alpha-2'), max_length=2, unique=True)
    name = models.CharField(_('Official name (CAPS)'), max_length=128)
    printable_name = models.CharField(_('Country name'), max_length=128)
    iso3_code = models.CharField(_('ISO alpha-3'), max_length=3, unique=True)
    numcode = models.PositiveSmallIntegerField(_('ISO numeric'), null=True, blank=True)
    continent = models.CharField(_('Continent'), choices=CONTINENTS, max_length=2)
    active = models.BooleanField(_('Country is active'), default=True)

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')
        ordering = ('name',)

    def __unicode__(self):
        return self.printable_name


class State(models.Model):
    """
    Administrative division for a country. State is a generic name, for some countries this 
    is equivalent to Province/Region/Territories/Departments
    """
    country = models.ForeignKey(Country)
    name = models.CharField(_('State/Province name'), max_length=60)
    abbr = models.CharField(_('State/Province Abbreviation'), max_length=3, null=True, blank=True)
    active = models.BooleanField(_('State/Province is active'), default=True)

    class Meta:
        verbose_name = _('State/Province')
        verbose_name_plural = _('States/Provinces')
        ordering= ('name',)

    def __unicode__(self):
        return self.name

