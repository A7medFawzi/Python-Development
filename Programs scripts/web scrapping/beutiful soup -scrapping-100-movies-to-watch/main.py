import requests
from bs4 import BeautifulSoup
import  lxml

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

respone = requests.get(URL)

empironline_website = respone.text

soup = BeautifulSoup(empironline_website, "html.parser")

movies_list = soup.findAll(name="h3", class_="title")

movies_name = []
for moive in movies_list:
    moive_name = moive.text
    movies_name.append(moive_name)


movirs_list = movies_name[::-1]

with open("moives.txt",mode="w") as file :
    for moive in movirs_list:
        file.write(f"{moive}\n")

