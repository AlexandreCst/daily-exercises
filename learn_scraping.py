"""Exercises to learn web scraping"""

import requests
from bs4 import BeautifulSoup

# ==================================================================
# Exercise 1 & 2: Scrape first page of http://books.toscrape.com/
# and display title, price, availability and rate for each book 
# ==================================================================

response = requests.get("http://books.toscrape.com/") # Get data of the website
response.encoding = "utf-8" # Define the data response encoding
print(f"Response status: {response.status_code}\n") # Check the request status


html = response.text # Get the data of the request in string
soup = BeautifulSoup(html, "html.parser") # Parse the response string

books = soup.find_all("article", class_="product_pod") # Search all books on page 1
resume = [] # Get the title, price, availability and rating of each book
for book in books:
    book_title = book.find("a", title=True)["title"]
    book_price = book.find("p", class_="price_color").get_text(strip=True)
    book_availability = book.find("p", class_="instock availability").get_text(strip=True)
    book_rating = book.find("p", class_="star-rating")["class"][1]

    resume.append((book_title, book_price, book_availability, book_rating))
    
print(resume)