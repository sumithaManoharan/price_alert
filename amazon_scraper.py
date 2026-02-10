import os
import smtplib
import requests as rt
from bs4 import BeautifulSoup as bs
from email.message import EmailMessage

my_email = os.environ.get("ZOHO_EMAIL")
zoho_password = os.environ.get("ZOHO_PASSWORD")

api_url = "https://www.amazon.in/gp/product/B0D73LWVF9/ref=ox_sc_act_title_1?smid=AXOGFIT0PZZ7G&th=1"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Not;A=Brand";v="99", "Brave";v="139", "Chromium";v="139"',
    "sec-ch-ua-full-version-list": '"Not;A=Brand";v="99.0.0.0", "Brave";v="139.0.0.0", "Chromium";v="139.0.0.0"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-ch-ua-platform-version": '"6.14.0"',
    "upgrade-insecure-requests": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Referer": "https://www.google.com/",
    "Connection": "keep-alive",
}
session = rt.Session()
session.headers.update(headers)
response = session.get(api_url)
data = bs(response.text, "html.parser")


# product_data = rt.get(api_url,headers=headers)
# product_data.raise_for_status()
# data = bs(product_data.text, "html.parser")

# title=data.select_one("span#productTitle").text
# price=data.select_one("span.a-price-whole").text.replace(",","").strip(".").strip(" ")


with smtplib.SMTP('smtp.zoho.in', 587) as connection:
    connection.starttls()
    connection.login(my_email, zoho_password)
    msg = EmailMessage()
    msg["Subject"] = "PRICE ALERT"
    msg["From"] = my_email
    msg["To"] = "sumithamanoharan76@gmail.com"
    if int(price) < 44990:
        body = f"PRICE ALERT! {title} price decreased to {price}\nCHECK OUT: {api_url}"
    else:
        body = f"No price decreased for {api_url}"
    msg.set_content(body)
    connection.send_message(msg)


