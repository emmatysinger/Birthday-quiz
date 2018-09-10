"""
birthday.py
Author: Emma
Credit: Tysinger
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth=datetime.today().month
todaydate=datetime.today().day
todaymonth=month_name[todaymonth]
todaymonth=todaymonth.lower()

name=input("Hello, what is your name? ")
month=input("Hi{0}, what was the name of the month you were born in? ".format(name))
month=month.lower()
year=input("And what year were you born in, {0}? ".format(name))
day=input("And the day?")

if month=="october" and day=="31":
    print("You were born on Halloween!")
elif month==todaymonth and day==todaydate:
    print("Happy Birthday!")
elif month==december or month==january or month==february:
    season="winter"
    if year>=1980 and year<1990:
        print("{0}, you are a {1} baby of the eighties.".format(name,season))
    elif year>=1990 and year<1999:
        print("{0}, you are a {1} baby of the nineties.".format(name,season))
    elif year>=2000:
        print("{0}, you are a {1} baby of the two thousands.".format(name,season))
    else:
         print("{0}, you are a {1} baby of the Stone Age.".format(name,season))
elif month==march or month==april or month==may:
    season="spring"
    if year>=1980 and year<1990:
        print("{0}, you are a {1} baby of the eighties.".format(name,season))
    elif year>=1990 and year<1999:
        print("{0}, you are a {1} baby of the nineties.".format(name,season))
    elif year>=2000:
        print("{0}, you are a {1} baby of the two thousands.".format(name,season))
    else:
         print("{0}, you are a {1} baby of the Stone Age.".format(name,season))
elif month==june or month==july or month==august:
    season="summer"
    if year>=1980 and year<1990:
        print("{0}, you are a {1} baby of the eighties.".format(name,season))
    elif year>=1990 and year<1999:
        print("{0}, you are a {1} baby of the nineties.".format(name,season))
    elif year>=2000:
        print("{0}, you are a {1} baby of the two thousands.".format(name,season))
    else:
         print("{0}, you are a {1} baby of the Stone Age.".format(name,season))
else:
    season="fall"
    if year>=1980 and year<1990:
        print("{0}, you are a {1} baby of the eighties.".format(name,season))
    elif year>=1990 and year<1999:
        print("{0}, you are a {1} baby of the nineties.".format(name,season))
    elif year>=2000:
        print("{0}, you are a {1} baby of the two thousands.".format(name,season))
    else:
         print("{0}, you are a {1} baby of the Stone Age.".format(name,season))