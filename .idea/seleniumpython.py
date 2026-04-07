from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class store:
    def __init__(self):
        self.driver= webdriver.Chrome()
        self.driver.maximize_window()
        #Website URL
        self.url="https://adnabu-store-assignment1.myshopify.com/password"
        self.wait=WebDriverWait(self.driver,20)

    # login functionality
    def login(self,password):
        self.driver.get(self.url)
        self.wait.until(expected_conditions.element_to_be_clickable((By.ID,"password"))).send_keys(password, Keys.ENTER)

    #Search the product name
    def search(self,product_name):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//summary[@aria-label='Search']"))).click()
        self.wait.until(expected_conditions.element_to_be_clickable((By.ID,"Search-In-Modal"))).send_keys(product_name,Keys.ENTER)
        self.wait.until(expected_conditions.element_to_be_clickable((By.PARTIAL_LINK_TEXT,product_name))).click()

    #Add product to the cart
    def addtocart(self,product):
            self.wait.until(expected_conditions.element_to_be_clickable((By.ID,"ProductSubmitButton-template--19850788667482__main"))).click()
            cart= self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@aria-label='Your cart']")))
            if cart.is_displayed():
               print("Success Message:")
            else:
               print("Fail Message:")

shope=store()

try:
    shope.login("AdNabuQA")
    shope.search("The Collection Snowboard: Liquid")
    shope.addtocart("The Collection Snowboard: Liquid")
finally:
    shope.driver.quit()







