from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

version = Service(ChromeDriverManager().install())

browser = webdriver.Chrome(service=version)

browser.get('https://api.mziq.com/mzfilemanager/v2/d/25fdf098-34f5-4608-b7fa-17d60b2de47d/36b20418-bc5c-a006-fa11-2232e7ed8799?origin=2')
browser.find_element('xpath', '//*[@id="icon"]/iron-icon')