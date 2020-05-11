#pip install selenium==4.0.0a5
import os
import unittest
from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class HeaderText(unittest.TestCase):
    def setUp(self):
        options = EdgeOptions()
        options.use_chromium = True
        options.binary_location = "C:\\Program Files (x86)\\Microsoft\\Edge Dev\\Application\\msedge.exe"
        dir = os.path.dirname(os.path.realpath(__file__))
        edge_driver_path = dir + "\\edgedriver_win64\\msedgedriver.exe"
        self.service = Service(edge_driver_path)
        self.service.start()
        self.driver = Edge(options = options, service = self.service)        
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://localhost:4200")

    def test_HeaderText(self):
        headerText = self.driver.find_element(By.CSS_SELECTOR, "h1").get_attribute("innerText")
        self.assertEqual("todos", headerText)

    def tearDown(self):
        self.driver.quit()
        self.service.stop()

class AddAToDoText(unittest.TestCase):
    def setUp(self):
        options = EdgeOptions()
        options.use_chromium = True
        options.binary_location = "C:\\Program Files (x86)\\Microsoft\\Edge Dev\\Application\\msedge.exe"
        dir = os.path.dirname(os.path.realpath(__file__))
        edge_driver_path = dir + "\\edgedriver_win64\\msedgedriver.exe"
        self.service = Service(edge_driver_path)
        self.service.start()
        self.driver = Edge(options = options, service = self.service)        
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://localhost:4200")

    def test_AddToDo(self):
        inputElement = self.driver.find_element(By.CLASS_NAME, "new-todo")
        inputElement.send_keys("The test is adding this todo" + Keys.ENTER)
        addedToDoText = self.driver.find_element(By.XPATH, "//input[@class='toggle']/following-sibling::label").get_attribute("innerText")
        self.assertEqual("The test is adding this todo", addedToDoText)

    def tearDown(self):
        self.driver.quit()
        self.service.stop()

if __name__ == '__main__':
    unittest.main(warnings='ignore')