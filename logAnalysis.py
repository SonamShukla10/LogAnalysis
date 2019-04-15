#!/usr/bin/env python3

import psycopg2
import sys

DBNAME = "news"

def run(output):
    db = psycopg2.connect(database=DBNAME)
	c = db.cursor()
	c.execute(query)
	results = c.fetchall()
	db.close()
	return(results)
	
def get_articles():
    output = ("""select articles.title, count(*)
            from articles, JOIN log
            on substring(log.path,10,100) = articles.slug
            and log.status = '200 OK'
            group by articles.title 
			ORDER BY count DESC LIMIT 3; """)
			
			# EXECUTE 
	fetch_articles =  run(output)
	
	print('\n What are the most popular articles of all time?')
	
	for title, views in fetch_articles:
	    print("  "title + " - " + str(views) + "views\n")
		

def get_authors():
    output = (""" "SELECT name, count(*) as num FROM authors" +
              "INNER JOIN articles ON (authors.id = articles.author) " +
              "JOIN log ON (REPLACE(log.path, '/article/', '')=articles.slug) " +
              AND authors.id = articles.authors
            GROUP BY authors.name
            ORDER BY count DESC
			limit 3; """)

   # execute
    fetch_authors = run(output)
	
	print('\nWho are the most popular article authors of all time?\n')
	for name, views in fetch_authors:
	    print("  ", name, "-", views, "views")


def get_errors():
    output = (""" SELECT count(t1.status)*100.0/t2.total as percentage,t1.time::date
              FROM log AS t1
              JOIN (
              SELECT count(status) AS total,time::date
              FROM log
              GROUP BY time::date
              ) AS t2
              ON t1.time::date = t2.time::date where t1.status not like '%200%'
              GROUP BY t1.time::date,t2.total; """)
			
			# execute
		result_error = run(output)	
		
		print("\nOn which days did more than 1% of requests lead to errors?\n")
		 
		for errordate, errorto, http_request, in result_error:
		    print("    {:%B %d, %Y}  --  {:.2f}% errors".format(errdate, errorto))
			print('\n')
			
if __name__ == '__main__':
    get_articles()  
    
	get_authors()
	
	get_errors()		
			
