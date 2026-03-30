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

books = soup.find_all("li", class_=True)
#for book in books:
 #   print(book.get_text())

print(books)
#print(soup.prettify())
