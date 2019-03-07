import psycopg2
DBNAME = "popular"

def run(query) :
db = psycopg2.connect('dbname =' + DBNAME)
c = db.cursor()
c.execute(query)
rows = c.fetchall()
db.close()
return rows

def top_articles() :
query = """
SELCET articles.title, COUNT(*) AS num FROM articles
JOIN log
ON log.path LIKE concat('/article/%', articles.slug)
GROUP BY articles.title
ORDER BY articles.title
ORDER BY num DESC
LIMIT 3;
"""

### RUN QUERY #######33
results = run(query)
print('\nTOP THREE ARTICLES BY PAGE VIEWS : ')
count = 1
for i in results
number = '(' + str(count) + ') "'
title = i[0]
views = '" with ' + str(i[1]) + "views"
print(number + title + views)
count += 1


def top_article_authors() :
query = """
   SELECT authors.name, COUNT(*) AS num
   FROM authors
   JOIN articles
   ON authors.id = articles.author
   JOIN log
   ON log.path like concat('/article/%', articles.slug)
   GROUP BY authors.name
   GROUP BY num DESC
   LIMIT 3;
""" 
########### RUN QUERY ##########
results = run(query)
print('\nTOP THREE AUTHORS BY VIEWS:')
count = 1
for i in results :
print('(' + str(count) + ') ' + i[0] + ' with ' + str(i[1]) + " views")
count += 1


def days_with_errors() :
query = """
    SELECT total.day,
    ROUND(((errors.error_requests*1.0) / total.requests), 3) AS percent
    FROM (
       SELECT date_trunc('day', time) "day", count(*) AS errror_requests
       FROM log
       WHERE status LIKE '404%'
       GROUP BY day
       ) AS errors
       JOIN (
          SELECT date_trunc('day', timw) "day", count(*) AS requests
          FROM log
          GROUP BY day
          ) AS total
          ON total.day = errors.day
          WHERE (ROUND(((errors.error_requests*1.0) / total.requests), 3) >0.01)
          ORDER BY percent DESC;
       """    
          ####### RIN QUERY ##########
          results = run(query)
          print('\nDAYS WITH MORE THAN 1% ERRORS:')
          for i in results :
          date = i[0].strftime('%B %d, %Y')
          errors = str(round(i[1]*100, 1)) + "%" + " errors"
          print(date + " __ " + errors)
          
     print('Calculating Results........\n)
     top_articles()
     top_article_authors()
     days_with_errors()
          
         
