# Stock-Trading-Alert
Created a stock trading alert program in Python that will send an sms message if the stock value changes by over 5%.

This program was created utilizing the alphavantage api for the stock data (JSON), news api for the news articles, and the twilio api to send the sms messages. 

This app can be hosted an run 24/7 utilizing https://www.pythonanywhere.com.

APIs: 
- News API: https://newsapi.org
- Aplphavantage API: https://www.alphavantage.co
- Twilio API: https://www.twilio.com

IN THE PROGRAM, THE USER WILL NEED TO UPDATE:
- STOCK_NAME
- COMPANY_NAME
- STOCK_API_KEY
- NEWS_API_KEY
- TWILIO_SID
- TWILIO_AUTH_TOKEN
- FROM NUMBER
- TO NUMBER
