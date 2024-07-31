with open("index.html", "r", encoding="utf-8") as file:
    html_content = file.read()

with open("utils/news.html", "r", encoding="utf-8") as file:
    news_content = file.read()

# Finding the position to insert the news
insert_position = html_content.find('<news>') + 6

# Deleting the old news
html_content = html_content[:insert_position] + html_content[html_content.find("</news>") - 6 :]

# Inserting the new news
html_content = html_content[:insert_position] + news_content + html_content[insert_position:]

with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_content)

