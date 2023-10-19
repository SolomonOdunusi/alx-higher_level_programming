-- Lists all the cities of Cali found in usa db
SELECT id, name FROM cities
WHERE state_id = (
	      SELECT id FROM states
	      WHERE name = "California")
ORDER BY id;
