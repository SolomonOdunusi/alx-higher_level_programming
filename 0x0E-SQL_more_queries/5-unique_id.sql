-- Creates "unique_id" table
CREATE TABLE IF NOT EXISTS unique_id
       (id INT DEFAULT 1,
	       UNIQUE (ID),
	       name VARCHAR(256));
