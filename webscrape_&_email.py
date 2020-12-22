import requests
import bs4
import lxml
import datetime as dt
import time
import smtplib
from email.mime.text import MIMEText


def send_email():
    email = 'polina@zemlicka.info'
    password = '**********************'
    smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_object.ehlo()
    smtp_object.starttls()
    smtp_object.login(email, password)

    # EMAIL
    from_address = 'polina@zemlicka.info'
    to_address = recipients[k][1]
    subject = "Автоматизированный гороскоп от гениальной дочери"
    message = ("Привет!" + '\n\n' +
               "Вот ваш ежедневный гороскоп:" + '\n\n'
               + email_string_1
               + email_string_2 + '\n\n'
               + email_string_3)
    msg = MIMEText(("Subject: " + subject + '\n' + message), 'plain')
    smtp_object.sendmail(from_address, to_address, msg.as_string())


base_url_1 = 'https://www.astrology.com/horoscope/daily/'
base_url_2 = 'https://astroscope.ru/horoskop/ejednevniy_goroskop/'
base_url_3 = 'https://mon.astrocenter.fr/horoscope/quotidien/'
mom_ext = ['pisces.html', 'poissons']
dad_ext = ['leo.html', 'lion']
polina_ext = ['aquarius.html', 'verseau']

recipients = {'mom': [mom_ext, 'lidia64@gmail.com'],
              'dad': [dad_ext, 'slava@ehouse.ch'],
              'polina': [polina_ext, 'polina@zemlicka.info']}

while True:
    for k in recipients.keys():
        email_string_1 = ''
        res = requests.get(base_url_1 + recipients[k][0][0])
        soup = bs4.BeautifulSoup(res.text, "lxml")
        text_1 = soup.findAll('p')[0]
        text_1.getText()
        email_string_1 += text_1.getText()

        email_string_2 = ''
        res = requests.get(base_url_2 + recipients[k][0][0])
        res.encoding = 'utf-8'
        soup = bs4.BeautifulSoup(res.text, "lxml")
        text_2 = soup.select('.col-12')[0]
        email_string_2 += '\n\n' + text_2.getText().replace('\n', ' ').replace('\t', '')

        email_string_3 = ''
        res = requests.get(base_url_3 + recipients[k][0][1])
        soup = bs4.BeautifulSoup(res.text, "lxml")
        text_3 = soup.select('.article-horoscope')[0]
        one = text_3.getText()
        text_3_sub = soup.select('.all-horoscope-linked')[0]
        two = text_3_sub.getText()
        email_string_3 += one.replace(two, '').replace('\n', ' ').replace('\t', '')

        send_email()
        print('email sent')

    # send every 24 hrs
    time.sleep(60 * 60 * 24)

