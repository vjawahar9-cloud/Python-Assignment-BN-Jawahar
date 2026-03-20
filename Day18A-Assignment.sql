CREATE DATABASE userdb1;

USE userdb1;

CREATE TABLE userlogin (
    userid INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(30),
    userpassword VARCHAR(30)
);

insert into userlogin values(1,'jawahar','pass123');
insert into userlogin values(2,'mahesh','pass345');
insert into userlogin values(3,'jeeva','pass678');

select * FROM userlogin;

UPDATE userlogin
SET userpassword='newpass333'
WHERE userid=1;

DELETE FROM userlogin
WHERE userid=3;

SELECT * FROM userlogin WHERE userid=2;

SELECT * FROM userlogin WHERE username='mahesh';














