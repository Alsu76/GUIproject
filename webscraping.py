import bs4
import requests

# https://toscrape.com/
# GOAL: get every tile of every book with a 2 star rating

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
two_star_books = []


for page_num in range(1,51):
    scrape_url = base_url.format(page_num)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text, "lxml")
    books = soup.select('.product_pod')
    for book in books:
        if len(book.select('.star-rating.Two')) !=0:
            book_title = book.select('a')[1]['title']
            two_star_books.append(book_title)
            print(scrape_url,book_title)
print(two_star_books)
