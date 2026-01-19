import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="function")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


@pytest.fixture
def context(browser):
    context = browser.new_context(
        locale="en-US",
        timezone_id="UTC",
        geolocation={"latitude": 40.7128, "longitude": -74.0060},
        permissions=["geolocation"]
    )
    yield context
    context.close()

