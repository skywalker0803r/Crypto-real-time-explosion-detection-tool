
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import requests
from tqdm import tqdm

def send_message(title,text,email='skywalker0803r@gmail.com',password="wlqdsvznivzgdygs"):
  content = MIMEMultipart()
  content["subject"] = title
  content["from"] = email
  content["to"] = email
  content.attach(MIMEText(text))
  with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(email,password)
    smtp.send_message(content)

def get_ticker_at_specific_intervals(limit=1000,interval="15m"):
    def input_symbol_return_15m_info(symbol = "BTCUSDT",url = "https://api.binance.com/api/v3/klines",interval = interval):
        response = requests.get(f"{url}?symbol={symbol}&interval={interval}")
        data = response.json()
        weighted_average_price = data[0][6]
        volume = data[0][7]
        return float(weighted_average_price),float(volume)
    # get all symbol and caculate 15m_volume return type list(dict())
    url = "https://api.binance.com/api/v3/exchangeInfo"
    response = requests.get(url)
    symbol_list = []
    if response.status_code == 200:
        data = response.json()
        symbols = data['symbols']
        for symbol in symbols[:limit]:
            base_asset = symbol['baseAsset']
            quote_asset = symbol['quoteAsset']
            symbol_list.append(f"{base_asset}{quote_asset}")
    else:
        pass

    pbar = tqdm(total=len(symbol_list))
    for idx,symbol_name in tqdm(enumerate(symbol_list)):
        weighted_average_price,quoteVolume = input_symbol_return_15m_info(symbol = symbol_name)
        symbol_list[idx] = {
            'symbol':symbol_name,
            'quoteVolume':quoteVolume,
            'weighted_average_price':weighted_average_price,
            }
        pbar.update(1)
    pbar.close()
    return symbol_list


     