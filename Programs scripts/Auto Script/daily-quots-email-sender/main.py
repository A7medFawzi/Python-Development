import  datetime as dt
import smtplib
import random

my_email = "example@mail.com"
my_pass = "password"
recipent = "example@email.com"



my_date = dt.datetime.now()
week_day = my_date.weekday()

if week_day == 3:
    quotes = open(file="quotes.txt")
    the_quot = random.choice(quotes.readlines())

    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password=my_pass)
    connection.sendmail(from_addr=my_email, to_addrs=recipent, msg=f"subject:hello\n\n {the_quot}")
    connection.close()
