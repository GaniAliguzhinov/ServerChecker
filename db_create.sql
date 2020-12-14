CREATE DATABASE mydb;
CREATE USER mydbuser with PASSWORD 'mydbpassword';
ALTER ROLE mydbuser SET client_encoding TO 'utf8';
ALTER ROLE mydbuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE mydbuser SET timezone to 'Asia/Almaty';
GRANT ALL PRIVILEGES ON DATABASE mydb to mydbuser;
