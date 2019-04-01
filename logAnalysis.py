# !/usr/bin/env python

import psycopg2
import sys
DBNAME = "news"

value1 = "What are the most popular articles ?"

q1 = ("SELECT title, count(*) as views FROM articles \n"
           "  JOIN log\n"
           "    ON articles.slug = substring(log.path, 10)\n"
           "    GROUP BY title ORDER BY views DESC LIMIT 3;")
		  
value2 = "Who are the most popular article authors ?"

q2 = ("SELECT authors.name, count(*) as views\n"
           "    FROM articles \n"
           "    JOIN authors\n"
           "      ON articles.author = authors.id \n"
           "      JOIN log \n"
           "      ON articles.slug = substring(log.path, 10)\n"
           "      WHERE log.status LIKE '200 OK'\n"
           "      GROUP BY authors.name ORDER BY views DESC;")
		   
		   
value2 =  "On which days more than 1% of the requests led to error?"

q3 = ("SELECT round((stat*100.0)/visitors, 3) as\n"
           "        result, to_char(errortime, 'Mon DD, YYYY')\n"
           "        FROM errorcount ORDER BY result desc limit 1;")

def get_query(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(sql_query)
    result = c.fetchall()
    db.close()
    return result
	
result1 = get_query(query_1)
result2 = get_query(query_2)
result3 = get_query(query_3)

def print_result(list):
    for i in range(len(list)):
        title = list[i][0]
        rest = list[i][1]
        print("\t" + "%s - %d" % (title, rest) + " views")
    print("\n")
	
print(value1)
print_result(result1)
print(value2)
print_result(result2)
print(value3)
print("\t" + result3[0][1] + " - " + str(result3[0][0]) + "%")
	
