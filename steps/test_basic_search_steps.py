
import re

from playwright.sync_api import expect
from pytest_bdd import scenarios, given, when, then

from pages.home_page import HomePage

scenarios("../features/basic_search.feature")


@given('As a not logged user I navigate to homepage "https://www.kiwi.com/en/"')
def open_homepage(page):
    home = HomePage(page)
    home.open()


@when("I select one-way trip type")
def select_one_way_trip(page):
    home = HomePage(page)
    home.select_one_way_trip()


@when('I set departure airport to "RTM"')
def set_departure_airport(page):
    home = HomePage(page)
    home.set_departure_airport("RTM")


@when('I set arrival airport to "MAD"')
def set_arrival_airport(page):
    home = HomePage(page)
    home.set_arrival_airport("MAD")


@when("I set departure date to 1 week from today")
def set_departure_date(page):
    home = HomePage(page)
    home.set_departure_date(days_from_today=7)


@when('I uncheck "Check accommodation with booking.com"')
def uncheck_accommodation(page):
    home = HomePage(page)
    home.uncheck_accommodation()


@when("I click the search button")
def click_search_button(page):
    home = HomePage(page)
    home.click_search_button()


@then("I am redirected to the search results page")
def verify_redirect_to_results(page):
    expect(page).to_have_url(re.compile(r"/search/results/"))


