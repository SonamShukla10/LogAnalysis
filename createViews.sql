CREATE VIEW http_reqs AS 
SELECT time::date AS date, count(*) AS total_err
FROM log
WHERE status <> '200 OK'
GROUP BY date
ORDER BY date ASC;


CREATE VIEW http_reqs AS 
SELECT time::date AS date, count(*) AS totals
FROM log
GROUP BY date
ORDER BY date ASC;

