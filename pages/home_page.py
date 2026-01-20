from playwright.sync_api import Page
from datetime import datetime, timedelta


class HomePage:
    URL = "https://www.kiwi.com/en/"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)
        modal = self.page.locator('[data-test="ModalCloseButton"]')
        if modal.is_visible():
            modal.click()

    def select_one_way_trip(self):
        self.page.get_by_role("button", name="Return").click()
        self.page.locator('[data-test="ModePopupOption-oneWay"]').click()

    def set_departure_airport(self, airport_code: str):
        from_input = self.page.locator('[data-test="PlacePickerInput-origin"] input')
        from_input.click()
        from_input.fill("")
        from_input.press("Backspace")
        from_input.fill(airport_code)
        self.page.locator('[data-test="PlacePickerRow-city"]').first.click()

    def set_arrival_airport(self, airport_code: str):
        arrival_input = self.page.locator('[data-test="PlacePickerInput-destination"] input')
        arrival_input.click()
        arrival_input.fill("")
        arrival_input.press("Backspace")
        arrival_input.fill(airport_code)
        self.page.locator('[data-test="PlacePickerRow-city"]').first.click()

    def set_departure_date(self, days_from_today: int):
        self.page.locator('[data-test="SearchFieldDateInput"]').click()

        target_date = datetime.now() + timedelta(days=days_from_today)
        date_str = target_date.strftime("%Y-%m-%d")
        day_locator = self.page.locator(f'div[data-test="CalendarDay"][data-value="{date_str}"]')
        day_locator.wait_for(state="visible")
        day_locator.click()
        self.page.locator("[data-test='SearchFormDoneButton']").click()

    def uncheck_accommodation(self):
        checkbox = self.page.locator('[data-test="accommodationCheckbox"] input[type="checkbox"]')
        if checkbox.is_checked():
            checkbox.uncheck()

    def click_search_button(self):
        self.page.locator('[data-test="LandingSearchButton"]').click()
