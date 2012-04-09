from django import forms
from django.utils.translation import ugettext_lazy as _
from countries_states.models import Country
from django.db.models import Q


def countries():
    """Get country selections."""
    return Country.objects.filter(active=True)

def states_for_country(country=None, translator=_):
    """
    Get state selections based on the country parameter.
    """
    choices = [('', translator('Not Applicable'))]

    if country:
        states = country.state_set.filter(active=True)
        if states.count() > 0:
            choices = [('', translator('---Please Select---'))]
            choices.extend([(state.abbr or state.name, state.name) for state in states])

    return choices


class CountryStateForm(forms.Form):
    """
    A basic form for Country and State/Province.
    """
    country = forms.ModelChoiceField(queryset=countries(), required=True, label=_('Country'), empty_label=_('---Please Select---'))
    state = forms.CharField(max_length=30, required=False, label=_('State/Province'), widget=forms.Select(choices=states_for_country()))

    def __init__(self, *args, **kwargs):
        super(CountryStateForm, self).__init__(*args, **kwargs)

        if self.is_bound:
            # if the user has already chosen the country and submitted,
            # populate the states/provinces accordingly.

            country_obj = self.fields['country'].clean(self.data.get('country'))
            state_choices = states_for_country(country_obj)
            self.fields['state'] = forms.ChoiceField(label=_('State/Province'), 
                                                    choices=state_choices, 
                                                    required=len(state_choices) > 1)
    
    def clean_country(self):
        if not self.cleaned_data.get('country'):
            raise forms.ValidationError(_('This field is required.'))
        return self.cleaned_data['country']

    def _check_state(self, data, country):
        if country and country.state_set.filter(active=True):
            if not data:
                raise forms.ValidationError(_('State is required for your country.'))
            if (country.state_set
                    .filter(active=True)
                    .filter(Q(name__iexact=data) | Q(abbr__iexact=data))
                    .count() != 1):
                raise forms.ValidationError(_('Invalid State or Province.'))
    
    def clean_state(self):
        data = self.cleaned_data.get('state')

        country = self.fields['country'].clean(self.data.get('country'))
        if country == None:
            raise forms.ValidationError(_('This field is required.'))
        self._check_state(data, country)

        return data
