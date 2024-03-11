-- Drop tables if they exist
DROP TABLE IF EXISTS game;
DROP TABLE IF EXISTS action_figure;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS poster;

-- Create tables

CREATE TABLE game (
    game_id             SERIAL PRIMARY KEY,
    game_title          VARCHAR(50) NOT NULL UNIQUE,
    quantity            INT NOT NULL,
    price               DECIMAL(4,2) NOT NULL
);

CREATE TABLE action_figure (
    action_figure_id    SERIAL PRIMARY KEY,
    action_figure_title VARCHAR(50) NOT NULL UNIQUE,
    quantity            INT NOT NULL,
    price               DECIMAL(4,2)
);

CREATE TABLE poster (
    poster_id           SERIAL PRIMARY KEY,
    poster_title        VARCHAR(50) NOT NULL UNIQUE,
    quantity            INT NOT NULL,
    price               DECIMAL(4,2) NOT NULL
);

CREATE TABLE employee (
    employee_id         SERIAL PRIMARY KEY,
    employee_name       VARCHAR(50) NOT NULL UNIQUE,
    position            VARCHAR(50) NOT NULL,
    salary              DECIMAL(8,2) NOT NULL
);