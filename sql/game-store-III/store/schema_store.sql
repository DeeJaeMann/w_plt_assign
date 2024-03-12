-- Drop the table if it exists
DROP TABLE IF EXISTS game;
DROP TABLE IF EXISTS action_figure;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS poster;

-- Create Tables
CREATE TABLE game (
    game_id SERIAL PRIMARY KEY,
    game_title VARCHAR(255) 
        UNIQUE 
        NOT NULL 
        CHECK (game_title ~ '^[A-Z0-9][\w \-:''\\]+$'),
    quantity INT 
        NOT NULL 
        CHECK(quantity > 0 AND quantity < 51),
    price DECIMAL(5, 2) 
        NOT NULL 
        CHECK(price > 10 AND price < 60)
);

CREATE TABLE action_figure (
    id SERIAL PRIMARY KEY,
    action_figure_title VARCHAR(255) 
        UNIQUE 
        NOT NULL 
        CHECK(action_figure_title ~ '^[A-Z0-9][\w :''\-\\]'),
    quantity INT 
        NOT NULL 
        CHECK(quantity > 0 AND quantity < 31),
    price DECIMAL(5,2) 
        NOT NULL 
        CHECK(price > 9.99 AND price < 100.01)
);

CREATE TABLE employee (
    id SERIAL PRIMARY KEY,
    employee_name VARCHAR(255) 
        NOT NULL 
        CHECK(employee_name ~ '^([A-Z][A-Za-z]*) ([A-Z][A-Za-z]*\s?){1,2}$'),
    position VARCHAR(255) 
        NOT NULL 
        CHECK(
            position ~ '^Sales Associate|Store Manager|Inventory Clerk|Customer Service Representative|IT Specialist|Marketing Coordinator|Assistant Manager|Finance Analyst|Security Officer|HR Coordinator$'), -- match the words from the description
    salary DECIMAL(7,2)
        NOT NULL
        CHECK(salary > 34652.80 AND salary < 65000.00)
    -- 16.66 ~ 34652.80
    -- 31.25 ~ 65000.00
);

CREATE TABLE poster (
    id INT PRIMARY KEY,
    poster_title VARCHAR,
    quantity INT,
    price DECIMAL(4,2)
);

