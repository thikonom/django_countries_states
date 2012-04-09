from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^countries_states/$', 'countries_states.views.countries_states_view', name='countries-states'),
    url(r'^ajax_populate_states/$', 'countries_states.views.ajax_populate_states', name='populate-states'),
)

