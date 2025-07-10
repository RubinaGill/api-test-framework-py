import requests
from pytest_bdd import scenarios, given, when, then
from assertpy import assert_that

scenarios('features/user_management.feature')

@given('the API base URL is configured')
def configure_api_base_url(api_base_url):
    return api_base_url