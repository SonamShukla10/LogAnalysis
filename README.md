# MyRepo

This project will query a PostgreSQL database (called "news") located on a virtual machine using a python program in order to answer three questions.

1.What are the most popular three articles of all time?
2.Who are the most popular authors of all time?
3.On which days did more than 1% of requests lead to errors?

Prerequisites
Python 3.6.2 installed. To download - go to Python.org.
PostgreSQL.
Virtual machine (if using) configured. See this Vagrantfile for use.
Data downloaded. To download - go to news data. After downloading, unzip the file and place it in the vagrant directory - or whatever file is shared with your virtual machine.
Data loaded. To do this - cd into your vagrant directory and use the command psql -d news -f newsdata.sql.
Views in database "news" created. Download create_view.sql Two views are needed.
Run script psql -d news -f create_views.sql

Then, finally run python3 logAnalysis.py file.
If, the error is package psycopg2 does not not exist the firstly install  pip3 install psycopg2 --user
Then python logAnalysis.py
