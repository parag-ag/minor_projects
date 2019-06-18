This is a python script that reads a .txt file which contains mail data of an organization and calculates which organization has sent how many mails.

It then stores data in a sqlite database with following schema.

CREATE TABLE Counts(org TEXT, count INTEGER) 
