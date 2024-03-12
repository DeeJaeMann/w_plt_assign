-- Drop tables if they exist
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS task;
DROP TABLE IF EXISTS timesheet;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS inventory;

-- Create tables
CREATE TABLE employee (
    id          SERIAL PRIMARY KEY,
    first_name  VARCHAR(30) NOT NULL,
    last_name   VARCHAR(30) NOT NULL
);

CREATE TABLE task (
    id          SERIAL PRIMARY KEY,
    type        VARCHAR(50) NOT NULL
);

CREATE TABLE timesheet (
    id          SERIAL PRIMARY KEY,
    employee_id BIGINT NOT NULL,
    task_id     BIGINT NOT NULL,
    start_time  TIMESTAMP NOT NULL,
    end_time    TIMESTAMP NOT NULL
);

CREATE TABLE product (
    id          SERIAL PRIMARY KEY,
    type        VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE sales (
    id          SERIAL PRIMARY KEY,
    revenue     DECIMAL(5,2) NOT NULL,
    product_id  BIGINT NOT NULL,
    quantity    INT NOT NULL
);

CREATE TABLE inventory (
    id          SERIAL PRIMARY KEY,
    quantity    INT NOT NULL,
    type        VARCHAR(50) NOT NULL UNIQUE
);

