-- settings.sql
CREATE DATABASE donor;
CREATE USER donoruser WITH PASSWORD 'supersecure';
GRANT ALL PRIVILEGES ON DATABASE donor TO donoruser;