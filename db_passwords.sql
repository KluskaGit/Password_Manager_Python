DROP DATABASE IF EXISTS m28441_passwords_manager;
CREATE DATABASE m28441_passwords_manager;
USE m28441_passwords_manager;

DROP TABLE IF EXISTS users;

CREATE TABLE all_passwords
(
    pass_id int(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    user_id int(11) NOT NULL,
    platform varchar(255),
    password varchar(255)
);

CREATE TABLE users
(
    user_id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email varchar(255) NOT NULL,
    password varchar(255) NOT NULL
);

ALTER TABLE all_passwords
ADD CONSTRAINT FOREIGN KEY (user_id) REFERENCES users (user_id); 
