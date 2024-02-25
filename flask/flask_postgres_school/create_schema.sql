-- Schema
DROP TABLE IF EXISTS addresses;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS subjects;

CREATE TABLE student (
    id          serial PRIMARY KEY,
    first_name  varchar(30) NOT NULL,
    last_name   varchar(30) NOT NULL,
    age         int NOT NULL,
    subject     int NOT NULL
);

CREATE TABLE teachers (
    id          serial PRIMARY KEY,
    first_name  varchar(30) NOT NULL,
    last_name   varchar(30) NOT NULL,
    age         int NOT NULL,
    subject     int NOT NULL
);

CREATE TABLE subjects (
    id          serial PRIMARY KEY,
    subject     varchar(20) NOT NULL
);
