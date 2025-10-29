from bs4 import BeautifulSoup
import requests

# Since we were getting 403 errors from the website then we had to give it a User agent header 
# otherwise we didn't have to write this code

headers = { 
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    )
}
# we send a requests.get to the website that we want to scrap
#if we get 200 respons that mean we got the information / if its 403 it means accese denied 

html_text = requests.get('https://www.goodreads.com/review/list/5387467-mohammad-efazati', headers=headers ).text

soup = BeautifulSoup(html_text, "lxml")
books = soup.find_all("tr", class_="bookalike review")
for book in books:
    book_name = book.find('a', title=True)
    print(book_name['title'])