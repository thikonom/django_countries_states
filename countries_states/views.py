from django.utils.translation import ugettext
from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render
from countries_states.forms import CountryStateForm, states_for_country


def countries_states_view(request):
    """
    A simple view that processes the CountriesStatesForm.
    """
    if request.method == 'POST':
        form = CountryStateForm(request.POST)
        if form.is_valid():
            message = 'You selected %s' % form.cleaned_data['country']
            if form.cleaned_data['state']:
                message += 'and %s' % form.cleaned_data['state']
            return HttpResponse(message)
    else:
        form = CountryStateForm()

    return render(request, 'base.html', {
            'form': form
        })

def ajax_populate_states(request):
    """
    Populates the states dropdown with the appropriate states.
    """
    formdata = request.REQUEST.copy()

    if 'country' in formdata:
        country_field = 'country'
    else:
        return HttpResponseServerError()

    form = CountryStateForm(data=formdata)
    country_data = formdata.get(country_field)

    try:
        country_obj = form.fields[country_field].clean(country_data)
    except:
        raise HttpResponseServerError()

    states = states_for_country(country_obj, ugettext)

    return render(request, 'state_choices.html', {
        'states': states    
    })

    



