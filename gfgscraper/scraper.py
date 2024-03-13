import requests
from bs4 import BeautifulSoup

def extract_links():
    """Extract links from a Beautiful Soup object based on a class name."""
    baseUrl = 'https://www.geeksforgeeks.org/learn-data-structures-and-algorithms-dsa-tutorial/?ref=ghm'
    response = requests.get(baseUrl)
    soup = BeautifulSoup(response.content, 'html.parser')

    leftSideNavigationPanel = soup.find('div', class_="sideBar--wrap")

    return [a['href'] for a in leftSideNavigationPanel.find_all('a', href=True)]

def download_page(url):
    # Make a request to the website
    response = requests.get(url)

    # Parse the page using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.title.string

    if ("GeeksforGeeks" not in title):
        return

    with open("articles/" + title + '.html', 'w', encoding='utf-8') as file:
        file.write(response.text)

for link in extract_links():
    download_page(link)
    # print(link)
    print("SUCCESS")