#!/usr/bin/python

from behave import given, when, then, step
from step_implementation import *

list_var = []


@given(u'Initialize browser setup')
def step_impl(context,):
    impl_obj.initialize_browser_setup(list_var)


@when(u'Open About page "{url_about_page}"')
def step_impl(context,url_about_page):
    impl_obj.open_About_page(list_var, url_about_page)


@when(u'Search for a person "{person_name}"')
def step_impl(context, person_name):
    impl_obj.search_for_a_person(list_var, person_name)


@then(u'Validate profile "{person_name}"')
def step_impl(context, person_name):
    impl_obj.validate_profile(list_var,person_name)


@when(u'Sort by options')
def step_impl(context,):
    impl_obj.sort_by_options(list_var,)


@then(u'Validate test run success')
def step_impl(context,):
    impl_obj.final_verification(list_var)
