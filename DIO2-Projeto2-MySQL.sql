CREATE TABLE movies(
	id INT PRIMARY KEY AUTO_INCREMENT,
	type INT NOT NULL,
	name VARCHAR(30) NOT NULL,
	total_ep INT,
	atual_ep INT,
	last_view DATE DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO movies(type, name, total_ep, atual_ep) VALUES (0,"Friends",10,1);

INSERT INTO movies(type, name) VALUES (1,"Avengers");

UPDATE movies SET last_view='2021-02-26' WHERE id=1;

INSERT INTO movies(type, name, total_ep, atual_ep, last_view) VALUES (0,"Todo mundo odeia o Chris",20,1,"2021-02-23");
INSERT INTO movies(type, name) VALUES (1,"1917");
INSERT INTO movies(type, name) VALUES (1,"300");

DELETE FROM movies id = 4;
