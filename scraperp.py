from bs4 import BeautifulSoup

with open ("index.html", "r") as html_file : # Request where  you want to scrape
    content = html_file.read()

    soup = BeautifulSoup(content, "lxml") # Make a soup curser i guess?
    course_cards = soup.find_all("div", class_='card')
    for course in course_cards:
        card_name = course.h5.text
        card_price = course.a.text.split()[-1]
        print(card_name,"costs",card_price)
