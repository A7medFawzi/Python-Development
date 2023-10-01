import pandas
import smtplib
import datetime as dt
import random

MY_EMAIL = "example@mail.com"
PASSWORD = "yourpassword"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

birthday_dic = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

for today_tuple in birthday_dic:
    person_birhdaty = birthday_dic[today_tuple]
    file_path = f"letter_templates\letter_{random.randint(1, 3)}.txt"

    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", person_birhdaty["name"])

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=person_birhdaty["email"],
                            msg=f"subject:Happy Birthday {person_birhdaty['name']} \n\n {contents}")
