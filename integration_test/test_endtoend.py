import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class TestEndToEnd(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options)
        self.driver.get('http://localhost:5000')

    def tearDown(self):
        self.driver.quit()

    def test_add_and_delete_and_update_item(self):
        self.driver.get("http://localhost:5000/")
        self.driver.set_window_size(1552, 936)
        self.driver.find_element(By.NAME, "item").click()
        self.driver.find_element(By.NAME, "item").send_keys("test1")
        self.driver.find_element(By.CSS_SELECTOR, "button").click()
        self.driver.find_element(By.NAME, "item").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".container > form > button")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.NAME, "item").send_keys("test2")
        self.driver.find_element(By.CSS_SELECTOR, ".container > form > button").click()
        self.driver.find_element(By.NAME, "new_item").click()
        self.driver.find_element(By.NAME, "new_item").send_keys("rename test1")
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) button").click()
        self.driver.find_element(By.LINK_TEXT, "Delete").click()
        self.driver.find_element(By.LINK_TEXT, "Delete").click()


if __name__ == "__main__":
    unittest.main()
