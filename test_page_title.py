
import requests
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options


def test_page_title():
    page_title_url = "https://en.wikipedia.org/w/api.php?action=query&titles=NASA&format=json"
    response = requests.get(page_title_url)
    if response.status_code == 200:
        data = response.json()
        page_title = list(data['query']['pages'].values())[0]['title']
        print("Page Title Endpoint:")
        print("Page Title:", page_title)
        print("Status: Success\n")
    else:
        print("Page Title Endpoint:")
        print("Status: Error -", response.status_code, response.reason, "\n")

if __name__ == "__main__":
    test_page_title()
