import requests
from twilio.rest import Client

STOCK_NAME = "STOCK NAME HERE"
COMPANY_NAME = "COMPANY NAME HERE"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "STOCK API KEY HERE"
NEWS_API_KEY = "NEWS STOCK API KEY HERE"
TWILIO_SID = "TWILIO SID HERE"
TWILIO_AUTH_TOKEN = "TWILIO AUTH TOKEN HERE"

# holding yesterdays closing price
# fetching from stock endpoint
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]


# Holding the day before yesterday's stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]


# finding the difference between the closing prices
difference = (float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
up_down = None
if difference > 5:
    up_down = "🔺"
else:
    up_down = "🔻"

# Finding the percentage difference
diff_percent = round((difference / float(yesterday_closing_price)) * 100)


# Updating with news if the percentage is greater than 5 and using the news api to send articles related to the company
if diff_percent > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    # using the python slice operator to only send the first three articles
    three_articles = articles[:3]

# creating a list of the first three articles

formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\n\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

# Send the message using twilio api
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_="FROM NUMBER HERE",
        to="TO NUMBER HERE",
    )


