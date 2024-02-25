-- Schema
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS students;

CREATE TABLE student (
    id          serial PRIMARY KEY,
    first_name  varchar(50) NOT NULL,
    last_name   varchar(50) NOT NULL,
    age         integer,
    grade       char(1)
);