# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 21:03:54 2024

@author: zhoushus
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DataScraper:
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.driver = None
        self.wait = None

    def setup_driver(self):
        # Set up the Edge WebDriver with headless mode
        options = Options()
        options.add_argument("--headless")
        service = Service(executable_path=self.driver_path)
        self.driver = webdriver.Edge(service=service, options=options)
        self.wait = WebDriverWait(self.driver, 120)

    def open_url(self, url):
        # Open the target URL
        self.driver.get(url)

    def select_category(self, category_xpath):
        try:
            # Scroll to and click the category link
            category = self.wait.until(EC.presence_of_element_located((By.XPATH, category_xpath)))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", category)
            self.driver.execute_script("arguments[0].click();", category)
            time.sleep(2)
        except Exception as e:
            raise RuntimeError(f"Error selecting category: {e}")

    def search_product(self, product_name, search_input_id, search_button_id):
        try:
            # Input the product name and click the search button
            prod_name_input = self.wait.until(EC.presence_of_element_located((By.ID, search_input_id)))
            prod_name_input.clear()
            prod_name_input.send_keys(product_name)
            search_button = self.driver.find_element(By.ID, search_button_id)
            self.driver.execute_script("arguments[0].click();", search_button)
            time.sleep(5)
        except Exception as e:
            raise RuntimeError(f"Error searching for product {product_name}: {e}")

    def extract_table_data(self, table_id):
        try:
            # Extract data rows from the result table
            table = self.driver.find_element(By.ID, table_id)
            rows = table.find_elements(By.TAG_NAME, 'tr')
            return [[col.text for col in row.find_elements(By.TAG_NAME, 'td')] for row in rows]
        except Exception as e:
            raise RuntimeError(f"Error extracting table data: {e}")

    def close_driver(self):
        # Close the browser and release resources
        if self.driver:
            self.driver.quit()
