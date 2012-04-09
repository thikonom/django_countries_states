Django Countries States
===============

A simple application that provides you with:

- Country and State models
- Fixtures for all Countries and States
- A simple form that populates the states based on the selection of the country via ajax/javascript


_State is just a generic name, for some countries this is equivalent to Province/Region/Territory/Department_


Installation
---------

+ Add 'countries_states' to your INSTALLED APPS
+ Add to your urls.py:
    + from countries_states.urls import urlpatterns as csurls
    + urlpatterns += csurls
+ Head to http://127.0.0.1:8000/countries_states/ 