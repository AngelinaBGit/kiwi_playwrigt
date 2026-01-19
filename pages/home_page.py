from playwright.sync_api import Page, expect
from datetime import datetime, timedelta


class HomePage:
    URL = "https://www.kiwi.com/en/"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)
        self.page.click("button[data-test='ModalCloseButton']")

    def select_one_way_trip(self):
        self.page.get_by_role("button", name="Return").click()
        self.page.locator('[data-test="ModePopupOption-oneWay"]').click()
        # page.get_by_role("option", name="One-way").click()

    def set_departure_airport(self, airport_code: str):
        from_input = self.page.locator('[data-test="PlacePickerInput-origin"] input')
        from_input.click()
        from_input.fill("")  # ensure input is empty
        from_input.press("Backspace")

        self.page.wait_for_timeout(300)

        from_input.fill(airport_code)
        self.page.wait_for_timeout(300)

        self.page.get_by_role("button", name="Rotterdam").click()

    def set_arrival_airport(self, airport_code: str):
        arrival_input = self.page.locator('[data-test="PlacePickerInput-destination"] input')
        arrival_input.click()
        arrival_input.fill("")
        arrival_input.press("Backspace")
        arrival_input.fill(airport_code)
        self.page.wait_for_timeout(300)
        self.page.locator(
            '[data-test="PlacePickerRow-city"]',
            has_text="Madrid"
        ).click()
        # self.page.locator('[data-test="PlacePickerRow-city"]').click()

    def set_departure_date(self, days_from_today: int = 7):
        self.page.locator('[data-test="SearchFieldDateInput"]').click()

        departure_day = 25

        month_button = self.page.locator('[data-test="DatepickerMonthButton"]').first
        month_button.click()

        month_container = month_button.locator('xpath=following-sibling::div[1]')

        # day_button = month_container.locator(f'button:has-text("{departure_day}")')
        day_button = month_container.locator(f'button:has(time[datetime="2026-01-25"])')

        day_button.click(force=True)

        self.page.locator("[data-test='SearchFormDoneButton']").click()

    def uncheck_accommodation(self):
        checkbox = self.page.locator(
            '[data-test="accommodationCheckbox"] input[type="checkbox"]'
        )

        checkbox.uncheck()

    def click_search_button(self):
        self.page.locator('[data-test="LandingSearchButton"]').click()
        expect(
            self.page.locator('[data-test="SortBy-quality"]')
        ).to_be_visible()
