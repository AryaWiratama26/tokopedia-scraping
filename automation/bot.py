from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os

load_dotenv()
LINK = os.getenv("LINK")


CHROME_DRIVER_PATH = "/usr/local/bin/chromedriver"

OP = webdriver.ChromeOptions()
# OP.add_argument('--headless')  

service = Service(executable_path=CHROME_DRIVER_PATH)

DRIVER = webdriver.Chrome(service=service, options=OP)


class TokopediaScraping:
    def __init__(self):
        self.url_tokped = LINK
        
    def search(self, keyword="sepatu"):
        try:
            
            DRIVER.get(self.url_tokped)
            
            search_data = WebDriverWait(DRIVER, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label='Cari di Tokopedia'][data-unify='Search']"))
            )
            
            search_data.send_keys(keyword)
            search_data.send_keys(Keys.ENTER)
            
            time.sleep(5)
        
        except Exception as e:
            print(f"Error search {e}")
            
    def get_price(self, data_len):
        try:
            
            data_harga = WebDriverWait(DRIVER, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[contains(text(),'Rp')]"))
            )
            
            for i in data_harga[:data_len]:
                print(i.text)
        
        except Exception as e:
            print(f"error get price {e}")
