CREATE DATABASE MasterMinds;

USE MasterMinds;

CREATE TABLE PlayerData(
	name TEXT,
	gameID int AUTO_INCREMENT,
	moves TEXT,
	attempts int,
	gameComplete boolean,
	PRIMARY KEY (gameID)
);


INSERT INTO PlayerData (name, moves, attempts, gameComplete) VALUES ('Muno', 'mmmm', '3', 0);



CREATE USER 'webapp'@'%' IDENTIFIED BY 'masterminds1';

GRANT ALL ON MasterMinds.* TO 'webapp'@'%';

