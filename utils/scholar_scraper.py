import requests
from bs4 import BeautifulSoup


def get_google_scholar_articles(profile_url):
    response = requests.get(
        profile_url,
        headers={
            "User-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
        },
    )
    soup = BeautifulSoup(response.text, "html.parser")

    html_content = ""
    for article in soup.find_all("tr", {"class": "gsc_a_tr"}):
        title = article.find("a", {"class": "gsc_a_at"}).text
        authors = article.find("div", class_="gs_gray").text
        journal = article.find("div", class_="gs_gray").find_next("div", class_="gs_gray").text
        year = article.find("td", {"class": "gsc_a_y"}).text

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
    profile_url = "https://scholar.google.com/citations?hl=en&user=kdJBxv8AAAAJ&view_op=list_works&sortby=pubdate"
    articles = get_google_scholar_articles(profile_url)
    html_template = f"""
    {articles}
    """
    with open("utils/scraped_publications.html", "w", encoding="utf-8") as html_file:
        html_file.write(html_template)
