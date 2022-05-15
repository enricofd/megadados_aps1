DROP DATABASE IF EXISTS mercearia;
CREATE DATABASE mercearia;

USE mercearia;

-- why use singular for table names
-- https://stackoverflow.com/a/5841297

DROP TABLE IF EXISTS cart;
CREATE TABLE cart (
	id_cart INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id_customer INT NOT NULL DEFAULT 1
);

DROP TABLE IF EXISTS product;
CREATE TABLE product (
	name VARCHAR(45) NOT NULL PRIMARY KEY,
    description VARCHAR(100) NOT NULL,
    price DECIMAL(2)
);

DROP TABLE IF EXISTS cart_product;
CREATE TABLE cart_product (
	id_cart INT NOT NULL PRIMARY KEY,
    name VARCHAR(45) NOT NULL PRIMARY KEY,
    quantity INT NOT NULL,
    CONSTRAINT fk_cart
		FOREIGN KEY (id_cart) 
            REFERENCES cart (id_cart) 
            ON DELETE CASCADE,
	CONSTRAINT fk_product
		FOREIGN KEY (name) 
            REFERENCES product (name) 
            ON DELETE CASCADE
);
