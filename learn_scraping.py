"""Exercises to learn web scraping"""

import requests
from bs4 import BeautifulSoup

# ==================================================================
# Exercise 1: Scrape first page of http://books.toscrape.com/
# and display title, price, availability and rate for each book 
# ==================================================================

response = requests.get("http://books.toscrape.com/")
print(f"Response status: {response.status_code}\n")
html = response.text
soup = BeautifulSoup(html, "html.parser")

html_books = soup.find_all("a", title=True)
books = []
for book in html_books:
    html_title = BeautifulSoup(str(book), 'html.parser')
    title = html_title.a['title']
    books.append(title)

prices = []
html_prices = soup.find_all("p", class_="price_color")
for price in html_prices:
    prices.append(price.get_text(strip=True).replace("Â", ""))


availabilities = []
html_availabilities = soup.find_all("p", class_="instock availability")
for availability in html_availabilities:
    availabilities.append(availability.get_text(strip=True))

rates = []
html_rates = soup.find_all("p", class_="star-rating")
for rate in html_rates:
    html_rate = BeautifulSoup(str(rate), "html.parser")
    rates.append(html_rate.p["class"][1])


resume = zip(books, prices, availabilities, rates)
for r in resume:
    print(r)
    
print(html_rates)



# print(books)
# print(prices)
# print(availabilities)
# print(soup.prettify())
