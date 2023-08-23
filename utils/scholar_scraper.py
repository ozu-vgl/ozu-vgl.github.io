import requests
from bs4 import BeautifulSoup
import time
import random

def scrape_google_scholar(username):
    base_url = f"https://scholar.google.com/citations?user={username}"
    articles = []

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    session = requests.Session()
    response = session.get(base_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    articles.extend(parse_articles(soup))

    while True:
        next_button = soup.find("button", {"id": "gsc_bpf_more"})
        if next_button:
            next_page_url = base_url + f"&cstart={len(articles)}"
            response = session.get(next_page_url, headers=headers)
            soup = BeautifulSoup(response.content, "html.parser")
            new_articles = parse_articles(soup)
            if not new_articles:
                break
            articles.extend(new_articles)
            delay = random.uniform(1, 3)
            time.sleep(delay)
        else:
            break

    return articles

def parse_articles(soup):
    articles = []
    item_list = soup.find_all("tr", {"class": "gsc_a_tr"})
    for article in item_list:
        if article.find("a", {"class": "gsc_a_at"}) and article.find("div", class_="gs_gray") and article.find("div", class_="gs_gray").find_next("div", class_="gs_gray") and article.find("td", {"class": "gsc_a_y"}):
            title = article.find("a", {"class": "gsc_a_at"}).text
            authors = article.find("div", class_="gs_gray").text
            journal = article.find("div", class_="gs_gray").find_next("div", class_="gs_gray").text
            year = article.find("td", {"class": "gsc_a_y"}).text
            print(title)

            articles.append({
                "title": title,
                "authors": authors,
                "journal": journal,
                "year": year
            })
    return articles

def to_html(articles):
    html_content = ""
    for article in articles:
        title = article["title"]
        authors = article["authors"]
        journal = article["journal"]
        year = article["year"]

        html_content += f"""<div class="publication-container">
        <div class="thumbnail-section">
            <img src="assets/publications/NTIRE_2023.png" alt="Thumbnail">
        </div>
        <div class="info-section">      
            <h3>{title}</h3>
            <p>Published in: {journal}</p>
            <p>Authors: {authors}</p>
            <p>Year: {year}</p>
        </div>
        </div>
    """
    return html_content

if __name__ == "__main__":
    username = "kdJBxv8AAAAJ&hl=en"
    articles = scrape_google_scholar(username)
    articles_html = to_html(articles)
    with open("utils/scraped_publications.html", "w", encoding="utf-8") as html_file:
        html_file.write(articles_html)
