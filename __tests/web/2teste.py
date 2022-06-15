
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestBlaze:
    def setup_method(self):
        self.driver = webdriver.Chrome('F:\\projetoPython\\134inicial-a\\vendors\\chromedriver\\chromedriver102.exe')
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_blaze(self):
        self.driver.get("https://www.blazedemo.com/")
        self.driver.set_window_size(1274, 728)
        self.driver.find_element(By.NAME, "fromPort").click()
        dropdown = self.driver.find_element(By.NAME, "fromPort")
        dropdown.find_element(By.XPATH, "//option[. = 'São Paolo']").click()
        self.driver.find_element(By.NAME, "toPort").click()
        dropdown = self.driver.find_element(By.NAME, "toPort")
        dropdown.find_element(By.XPATH, "//option[. = 'Rome']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .btn").click()
        self.driver.find_element(By.ID, "inputName").click()
        self.driver.find_element(By.ID, "inputName").send_keys("Jeferson")
        self.driver.find_element(By.ID, "address").send_keys("av rua")
        self.driver.find_element(By.ID, "city").click()
        self.driver.find_element(By.ID, "city").send_keys("indiara")
        self.driver.find_element(By.ID, "state").click()
        self.driver.find_element(By.ID, "state").send_keys("goiania")
        self.driver.find_element(By.ID, "cardType").click()
        dropdown = self.driver.find_element(By.ID, "cardType")
        dropdown.find_element(By.XPATH, "//option[. = 'Diner\'s Club']").click()
        self.driver.find_element(By.ID, "creditCardNumber").click()
        self.driver.find_element(By.ID, "rememberMe").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(2)").text == "Airline: United"
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == "Thank you for your purchase today!"
