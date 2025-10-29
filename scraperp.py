from bs4 import BeautifulSoup

with open ("index.html", "r") as html_file : # Request where  you want to scrape
    content = html_file.read()

    soup = BeautifulSoup(content, "lxml") # Make a soup curser i guess?
    courses_html_tags = soup.find_all('h5') #Search for tag and use find all to find all the tags not only first tag
    prices = soup.find_all('a') 
    for price,course in zip(prices,courses_html_tags): #zip them so we dont face valueerror
        print(price.text,course.text)
