CREATE TYPE ROLE AS ENUM('1', '0');

CREATE TABLE IF NOT EXISTS "user"(
    id bigserial not null primary key,
    name text,
    email text,
    password text,
    fund integer,
    phoneNumber text,
    role ROLE,
    positionID integer
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
    totalAmount integer
);


INSERT INTO "user"(name, email, password, fund, phoneNumber, role, positionID) values ('Kien', 'kien@gmail.com', '1', '1000', '0123456789', '1', '1');


