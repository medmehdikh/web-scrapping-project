from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json
import time
import os

DATA_FILE = "data/peugeot_2008_annonces.json"


def scrape_peugeot_2008():
    # Initialize Selenium WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    url = 'https://www.automobile.tn/fr/occasion/s=sort!-date/7/peugeot/2008/112331/peugeot/2008/112051/peugeot/2008/110734/peugeot/2008/99879'
    driver.get(url)

    # Wait for the page to load
    time.sleep(5)

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    annonces = []

    for ad in soup.find_all('div', class_='car-box'):
        try:
            title = ad.find('a', class_='car-title').text.strip()
            price = ad.find('span', class_='price').text.strip()
            year = ad.find('span', class_='year').text.strip()
            mileage = ad.find('span', class_='km').text.strip()
            location = ad.find('div', class_='location').text.strip()
            link = ad.find('a', class_='car-title')['href']

            annonces.append({
                'title': title,
                'price': price,
                'year': year,
                'mileage': mileage,
                'location': location,
                'link': link
            })
        except AttributeError:
            continue

    # Save the scraped data to a JSON file
    if annonces:
        with open(DATA_FILE, 'w') as f:
            json.dump(annonces, f, indent=4)

    driver.quit()

