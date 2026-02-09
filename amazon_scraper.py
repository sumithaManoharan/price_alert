import os
import smtplib
import requests as rt
from bs4 import BeautifulSoup as bs
from email.message import EmailMessage

my_email = os.environ.get("ZOHO_EMAIL")
zoho_password = os.environ.get("ZOHO_PASSWORD")

api_url = "https://www.amazon.in/gp/product/B0D73LWVF9/ref=ox_sc_act_title_1?smid=AXOGFIT0PZZ7G&th=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}
product_data = rt.get(api_url,headers=headers)
product_data.raise_for_status()
data = bs(product_data.text, "html.parser")

title=data.select_one("span#productTitle").text
price=data.select_one("span.a-price-whole").text.replace(",","").strip(".").strip(" ")


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


