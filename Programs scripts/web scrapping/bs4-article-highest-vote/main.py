import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")

yc_website =  response.text

soup = BeautifulSoup(yc_website,"html.parser")
article_tag = soup.findAll(name="a",class_="titlelink")
article_upvotes=  [int(score.text.split(" ")[0]) for score in soup.findAll(name="span",class_="score")]


article_texts = []
article_links = []
for article in article_tag:
    article_text = article.text
    article_texts.append(article_text)
    article_link = article.get("href")
    article_links.append(article_link)

largest_upvote = max(article_upvotes)
largest_upvote_index = article_upvotes.index(largest_upvote)


print(article_texts[largest_upvote_index])
print(article_links[largest_upvote_index])




