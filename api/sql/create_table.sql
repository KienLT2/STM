CREATE TYPE ROLE AS ENUM('1', '0');

CREATE TABLE IF NOT EXISTS "user"(
    id bigserial not null primary key,
    name text,
    email text,
    password text,
    fund integer,
    phonenumber text,
    role ROLE,
    positionid integer
);

CREATE TABLE IF NOT EXISTS "position"(
    id bigserial not null primary key,
    position text
);

CREATE TABLE IF NOT EXISTS "schedule"(
    id bigserial not null primary key,
    date DATE,
    time TIME,
    fieldfee integer,
    participants int[]
);

CREATE TABLE IF NOT EXISTS "fund"(
    id bigserial not null primary key,
    totalamount integer,
    editeddate timestamp
);


INSERT INTO "fund"(id, totalamount, editeddate) values (1, 123456789, '2016-06-22 19:10:25-07');


