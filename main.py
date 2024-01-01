import json
import requests

def sender(chat_id, message):
    api_token = "YOUR_API_TOKEN"  # Replace with your actual API token
    message = message.replace(" ", "%20")
    url = f"https://api.telegram.org/bot{api_token}/sendmessage?chat_id={chat_id}&text={message}"
    response = requests.get(url)

def table():
    url = "https://cdn.farabours.com/api/ClosingPrice/GetMarketMap?market=0&size=1366&sector=0&typeSelected=1&hEven=0"
    response = requests.get(url)
    return json.loads(response.text)

data = input()
with open('exam.json', 'w') as file:
    file.write(data)

datacod = json.loads(data)
id = datacod['message']['from']['id']
message = datacod['message']['text']

if message == '/help':
    textttt = "این ربات توسط دانشجویان درس مبانی کامپیوتر دکتر اسلامی در دانشگاه علوم و تحقیقات توسعه داده شده است"
    sender(id, textttt)
else:
    t = 0
    x = table()
    for v in x:
        symb = v['lVal18AFC']
        tilte = v['lVal30']
        message = json.loads('"' + message + '"')
        lastprice = v['pClosing']
        percent = v['percent']
        if message == symb:
            finetext = f"آخرین قیمت معامله شده سهم شرکت {tilte} برابر با {lastprice} ریال بوده و سود نهایی این شرکت در شبانه روز گذشته {percent} درصد بوده است."
            sender(id, finetext)
            t = 1
            break

    x = random.shuffle(x)
    if t < 1:
        result_list = []
        for z in range(10):
            v = x[z]
            symb = v['lVal18AFC']
            tilte = v['lVal30']
            result_list.append(f"{tilte} : {symb}")

        text1 = "برای دریافت آخرین وضعیت سهم بورسی، مد نظر خود میتوانید شناسه بورسی آن را وارد نمایید به طور مثال: " + ', '.join(result_list)
        sender(id, text1)
