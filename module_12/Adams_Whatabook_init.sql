-- Jennifer Adams
-- CYBR410-T301
-- WhatABook Scripts
-- August 9, 2022


-- drop database if exists --

DROP DATABASE IF EXISTS whatabook;

-- create database --
CREATE DATABASE whatabook;

-- use database --

USE whatabook;

-- drop user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- CREATING TABLES --

-- create table Book --
CREATE TABLE book (
  book_id int NOT NULL AUTO_INCREMENT,
  book_name varchar(200) NOT NULL,
  details varchar(500) DEFAULT NULL,
  author varchar(200) NOT NULL,
  PRIMARY KEY (book_id)
);

-- create table Store --
CREATE TABLE store (
  store_id int NOT NULL,
  locale varchar(500) NOT NULL,
  hours varchar(500) NOT NULL,
  PRIMARY KEY (store_id)
);

-- create table User --
CREATE TABLE user (
  user_id int NOT NULL AUTO_INCREMENT,
  first_name varchar(75) NOT NULL,
  last_name varchar(75) NOT NULL,
  PRIMARY KEY (user_id)
);

-- create table Inventory --
CREATE TABLE inventory (
  inventory_id int NOT NULL AUTO_INCREMENT,
  store_id int NOT NULL,
  book_id int NOT NULL,
  book_quantity int NOT NULL,
  PRIMARY KEY (inventory_id)
);

-- create table Wishlist --
CREATE TABLE wishlist (
  wishlist_id int NOT NULL AUTO_INCREMENT,
  user_id int NOT NULL,
  book_id int NOT NULL,
  PRIMARY KEY (wishlist_id)
);

-- POPULATING TABLES --

-- populate table Book --
INSERT INTO book(book_id, book_name, details, author)
   VALUES(1,'CompTIA Cloud Essentials+','McGraw-Hill Education 2020','Lachance, Daniel');

INSERT INTO book(book_id, book_name, details, author)
   VALUES(2,'Active Directory for Dummies','Wiley Publishing 2008','Clines, Steve & Loughry, Marcia');

INSERT INTO book(book_id, book_name, details, author)
   VALUES(3,'AI Ethics','MIT Press 2020','Coeckelbergh, Mark');

INSERT INTO book(book_id, book_name, details, author)
   VALUES(4,'NoSQL Distilled','Pearson Education, Inc. 2013','Sadalage, Pramod & Fowler, Martin');

INSERT INTO book(book_id, book_name, details, author)
   VALUES(5,'NoSQL for Dummies','John Wiley & Sons, Inc. 2015','Fowler, Adam');

INSERT INTO book(book_id, book_name, details, author)
   VALUES(6,'Sams Teach Yourself SQL in 10 Minutes','Pearson Education, Inc. 2020','Forta, Ben');

INSERT INTO book(book_id, book_name, details, author)
   VALUES(7,'Sams Teach Yourself SQL in 24 Hours','Sams Publishing 1998','Stephens, Ryan & Plew, Ronald');

INSERT INTO book(book_id, book_name, details, author)
   VALUES(8,'Head First SQL','OReilly Media Inc. 2007','Beighley, Lynn');

INSERT INTO book(book_id, book_name, details, author)
   VALUES(9,'Networking All-in-One for Dummies','John Wiley & Sons, Inc. 2018','Lowe, Doug');

-- populate table Store --
INSERT INTO Store(store_id, locale, hours)
   VALUES(1,'123 Anyplace St., Anywhere US 12345', '9:00 AM to 6:00 PM Monday through Friday');

-- populate table User --
INSERT INTO User(user_id, first_name, last_name)
   VALUES(1, 'Jane', 'Doe');

INSERT INTO User(user_id, first_name, last_name)
   VALUES(2, 'Alice', 'Wonderland');

INSERT INTO User(user_id, first_name, last_name)
   VALUES(3, 'Bob', 'Barker');

-- populate table Inventory --
INSERT INTO Inventory(inventory_id, store_id, book_id, book_quantity)
   VALUES(123321,1,1,3);

INSERT INTO Inventory(inventory_id, store_id, book_id, book_quantity)
   VALUES(123322,1,2,2);

INSERT INTO Inventory(inventory_id, store_id, book_id, book_quantity)
   VALUES(123323,1,3,5);

INSERT INTO Inventory(inventory_id, store_id, book_id, book_quantity)
   VALUES(123324,1,4,4);

INSERT INTO Inventory(inventory_id, store_id, book_id, book_quantity)
   VALUES(123325,1,5,7);

INSERT INTO Inventory(inventory_id, store_id, book_id, book_quantity)
   VALUES(123326,1,6,2);

INSERT INTO Inventory(inventory_id, store_id, book_id, book_quantity)
   VALUES(123327,1,7,5);

INSERT INTO Inventory(inventory_id, store_id, book_id, book_quantity)
   VALUES(123328,1,8,3);

INSERT INTO Inventory(inventory_id, store_id, book_id, book_quantity)
   VALUES(123329,1,9,6);

-- populate table Wishlist --
INSERT INTO Wishlist(wishlist_id, user_id, book_id)
   VALUES(100,3,2);

INSERT INTO Wishlist(wishlist_id, user_id, book_id)
   VALUES(200,1,5);

INSERT INTO Wishlist(wishlist_id, user_id, book_id)
   VALUES(300,2,1);

-- ADDING FOREIGN KEYS --

-- add foreign keys to Inventory --
ALTER TABLE Inventory
   ADD FOREIGN KEY (store_id) REFERENCES Store(store_id);

ALTER TABLE Inventory
   ADD FOREIGN KEY (book_id) REFERENCES Book(book_id);

-- add foreign keys to Wishlist --
ALTER TABLE Wishlist
   ADD FOREIGN KEY (user_id) REFERENCES User(user_id);

ALTER TABLE Wishlist
   ADD FOREIGN KEY (book_id) REFERENCES Book(book_id);