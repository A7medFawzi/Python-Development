import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

URL = "https://www.amazon.com/Acer-AN515-55-53E5-i5-10300H-GeForce-Keyboard/dp/B092YHJGMN/ref=sr_1_2?qid=1651807554" \
      "&rnid=16225007011&s=computers-intl-ship&sr=1-2 "
headers= {
    "Accept-Language":"en-US,en;q=0.9,ar;q=0.8",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/100.0.4896.127 Safari/537.36 "
}

response = requests.get(URL,headers=headers)
website_data = response.text

soup = BeautifulSoup(website_data,"lxml")
product_price = float(soup.find(name="span",class_="a-offscreen").get_text().split("$")[1])
print(product_price)


title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 700

if product_price < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("gamil.smtp", port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
