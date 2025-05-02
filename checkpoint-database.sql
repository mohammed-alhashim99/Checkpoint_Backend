-- DROP DATABASE IF EXISTS checkpoint;
-- DROP ROLE IF EXISTS checkpoint_admin;

CREATE DATABASE checkpoint;

CREATE USER checkpoint_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE checkpoint TO checkpoint_admin;
