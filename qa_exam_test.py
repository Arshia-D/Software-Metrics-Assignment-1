import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains


class TestExitIntent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        cls.driver.implicitly_wait(3)
        cls.base_url = "https://the-internet.herokuapp.com/exit_intent"

    def test_exit_intent(self):
        with self.driver as driver:
            driver.get(self.base_url)
            body = driver.find_element(By.TAG_NAME, 'body')
            chains = ActionChains(driver)
            chains.move_to_element_with_offset(body, 0, 500).perform()
            wait = WebDriverWait(driver, 10)
            modal = wait.until(EC.visibility_of_element_located((By.ID, "ouibounce-modal")))
            self.assertTrue(modal.is_displayed())

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
