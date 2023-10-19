-- Displays top 3 cities during july and august
SELECT `city`, MAX(`value`) AS `max_temperature`
FROM `temperatures`
WHERE `month` = 7 OR `month` = 8
GROUP BY `city`
ORDER BY `max_temperature` DESC
LIMIT 3;
