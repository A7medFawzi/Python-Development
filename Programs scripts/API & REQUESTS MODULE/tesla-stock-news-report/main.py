import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

#https://www.alphavantage.co/query
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_KEY = ""

#https://newsapi.org/v2/everything
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_KEY = ""

stock_paramters = {

    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_KEY,
}

response_stock = requests.get(url=STOCK_ENDPOINT, params=stock_paramters)
response_stock.raise_for_status()

data = response_stock.json()

date_list = [key for (key, value) in data['Time Series (Daily)'].items()]

yesterday_date = date_list[0]
day_before_yasyerday = date_list[1]

yesterday_closing_price = float(data['Time Series (Daily)'][yester_day_date]['4. close'])
day_before_yasyerday_closing_price = float(data['Time Series (Daily)'][day_before_yasyerday]['4. close'])

difference_bettwn_2D = round(day_before_yasyerday_closing_price - yesterday_closing_price, 2)
difference_precentage = round(difference_bettwn_2D / day_before_yasyerday_closing_price * 100)

news_paramters = {

    "q": COMPANY_NAME,
    "apiKey": NEWS_KEY,
    "from": yester_day_date

}

response_news = requests.get(url=NEWS_ENDPOINT, params=news_paramters)
response_news.raise_for_status()

news_data = response_news.json()

articles = news_data['articles'][:3]

up_down = None

if difference_precentage > 0:
    up_down = "🢁"

else:
    up_down = "🢃"

for article in articles:
    print(f"TSLA: {up_down} {abs(difference_precentage)}% Headline: {article['title']} \n The URL: {article['url']}")
