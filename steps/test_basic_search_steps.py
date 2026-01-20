
import re

from playwright.sync_api import expect
from pytest_bdd import scenarios, given, when, then, parsers


scenarios("../features/basic_search.feature")


@given('As a not logged user I navigate to homepage "https://www.kiwi.com/en/"')
def open_homepage(home):
    home.open()


@when("I select one-way trip type")
def select_one_way_trip(home):
    home.select_one_way_trip()


@when(parsers.parse('I set departure airport to "{origin}"'))
def set_departure_airport(home, origin):
    home.set_departure_airport(origin)


@when(parsers.parse('I set arrival airport to "{destination}"'))
def set_arrival_airport(home, destination):
    home.set_arrival_airport(destination)


@when(parsers.parse('I set departure date to "{days}" days from today'))
def set_departure_date(home, days):
    home.set_departure_date(days_from_today=int(days))


@when('I uncheck "Check accommodation with booking.com"')
def uncheck_accommodation(home):
    home.uncheck_accommodation()


@when("I click the search button")
def click_search_button(home):
    home.click_search_button()


@then("I am redirected to the search results page")
def verify_redirect_to_results(page):
    expect(page).to_have_url(re.compile(r"/search/results/"))