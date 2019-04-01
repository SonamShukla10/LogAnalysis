-- Create views in 'news' postgreSQL db for use with
-- logs_analysis.py 

CREATE VIEW logstar AS
SELECT count(*) as stat, 
status, cast(time as date) as day
FROM log WHERE status like '%404%'
GROUP BY status, day
ORDER BY stat desc limit 3;

CREATE VIEW totalvisitors AS
SELECT count(*) as visitors,
cast(time as date) as errortime
FROM log
GROUP BY errortime;

CREATE VIEW errorcount AS
SELECT * from logstar join totalvisitors
ON logstar.day = totalvisitors.errortime;
