"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DuckDuckGoResultPage:

    RESULT_LINKS = (By.CSS_SELECTOR, "a.result__a") #'a[data-testid="result-title-a"]')
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='q']")

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)

    # --- waits ---

    def wait_for_results(self):
        """Wait until result links appear (indicates results page loaded)."""
        self.wait.until(EC.presence_of_element_located(self.RESULT_LINKS))

    # --- interaction methods ---

    def result_link_titles(self):
        self.wait_for_results()
        links = self.browser.find_elements(*self.RESULT_LINKS)
        return [link.text for link in links]

    def search_input_value(self):
        self.wait_for_results()
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        return search_input.get_attribute("value")

    def title(self):
        self.wait_for_results()
        return self.browser.title
