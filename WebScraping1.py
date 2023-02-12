from bs4 import BeautifulSoup
import time
import pandas as pd
import requests

START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

requests.get(START_URL)

time.sleep(10)

star_data = []

def scrape():
    for i in range(0, 10):
        print(f"Scrapping Page {i+1} ...")

        soup = BeautifulSoup(requests.page_source, "html.parcel")




scrape()

headers = ["name", "distance", "mass", "radius"]
