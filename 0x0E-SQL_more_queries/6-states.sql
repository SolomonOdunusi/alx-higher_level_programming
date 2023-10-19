-- Creates both database "usa" and table "states"
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	       id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
	       name VARCHAR(256) NOT NULL
);
