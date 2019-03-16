#!/usr/bin/env python3

import psycopg2
import sys

DBNAME = "news"


def execute_query(query):
    try:
        
        db = psycopg2.connect(database=DBNAME)
       
        c = db.cursor()
        
        c.execute(query)
        
        results = c.fetchall()
       
        db.close()
       
        return (results)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)



def get_articles():

    
    query = ("""
        SELECT title, count(title)
        FROM log, articles
        WHERE '/article/' || articles.slug = log.path
        GROUP BY title
        ORDER BY count DESC
        LIMIT 3""")
    
    pop_articles = execute_query(query)

    
    print('\nWhat are the most popular three articles of all time?\n')

   
    for title, views in pop_articles:
        lst = "  " + '"' + title + '"' + " - " + str(views) + " views\n"
        sys.stdout.write(lst)


def get_authors():

   
    query = ("""
        SELECT name, count(title)
        FROM log, articles, authors
        WHERE '/article/' || articles.slug = log.path
        AND authors.id = articles.author
        GROUP BY authors.name
        ORDER BY count DESC""")

    
    pop_authors = execute_query(query)

   
    print('\nWho are the most popular article authors of all time?\n')

  
    for name, views in pop_authors:
        print("  ", name, "-", views, "views")



def get_errors():

    # SQL to retrieve error codes more than 1% (from 2 diff views)
    query = ("""
        WITH t AS (
            SELECT tot_reqs.date,
                   round((tot_err::numeric / totals::numeric) * 100, 2)
                    AS pct_errs
            FROM err_reqs, tot_reqs
            WHERE err_reqs.date = tot_reqs.date
            )
        SELECT to_char(date, 'TMMonth DD"," YYYY'),
               pct_errs
        FROM t
        WHERE pct_errs > 1.0""")

    
    err_days = execute_query(query)

    
    print("\nOn which days did more than 1% of requests lead to errors?\n")

   
    for date, pct_errs in err_days:
        bad_status = "  " + date + " - " + str(pct_errs) + "% errors\n"
        sys.stdout.write(bad_status)
        print('\n')



if __name__ == '__main__':
    get_articles()

    get_authors()

    get_errors()
          
         
