
CREATE DATABASE IF NOT EXISTS userdb;


USE userdb;


CREATE TABLE IF NOT EXISTS userlogin (
    userid INT PRIMARY KEY,
    username VARCHAR(30),
    userpassword VARCHAR(30)
);


INSERT INTO userlogin VALUES (1,'Jawahar','pass123');
INSERT INTO userlogin VALUES (2,'Arun','arun123');
INSERT INTO userlogin VALUES (3,'Rahul','rahul123');


SELECT * FROM userlogin;


UPDATE userlogin
SET userpassword='newpass123'
WHERE userid=1;


DELETE FROM userlogin
WHERE userid=3;


SELECT * FROM userlogin WHERE userid=2;
SELECT * FROM userlogin WHERE username='Arun';



