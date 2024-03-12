-- Drop the table if it exists
DROP TABLE IF EXISTS game;
DROP TABLE IF EXISTS action_figure;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS poster;

-- Create Tables
CREATE TABLE game (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50) 
        UNIQUE 
        NOT NULL 
        CHECK (title ~ '^[A-Z0-9][\w \-:''\\]+$'),
    quantity INT 
        NOT NULL 
        CHECK(quantity > 0 AND quantity < 51),
    price DECIMAL(5, 2) 
        NOT NULL 
        CHECK(price > 10 AND price < 60)
);

CREATE TABLE action_figure (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50) 
        UNIQUE 
        NOT NULL 
        CHECK(title ~ '^[A-Z0-9][\w :''\-\\]'),
    quantity INT 
        NOT NULL 
        CHECK(quantity > 0 AND quantity < 31),
    price DECIMAL(5,2) 
        NOT NULL 
        CHECK(price > 9.99 AND price < 100.01)
);

CREATE TABLE employee (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) 
        NOT NULL 
        CHECK(name ~ '^([A-Z][A-Za-z]*) ([A-Z][A-Za-z]*\s?){1,2}$'),
    position VARCHAR(50) 
        NOT NULL 
        CHECK(
            position ~ '^Sales Associate|Store Manager|Inventory Clerk|Customer Service Representative|IT Specialist|Marketing Coordinator|Assistant Manager|Finance Analyst|Security Officer|HR Coordinator$'), -- match the words from the description
    salary DECIMAL(7,2)
        NOT NULL
        CHECK(salary > 31999.99 AND salary < 65000.01)
    -- 16.66 ~ 34652.80  one record set to 32000
    -- 31.25 ~ 65000.00
);

CREATE TABLE poster (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50)
        NOT NULL
        UNIQUE
        CHECK(title ~ '^[A-Z0-9][\w\-\s]*$'),
    quantity INT
        NOT NULL
        CHECK(quantity > 0 AND quantity < 31),
    price DECIMAL(4,2)
        NOT NULL
        CHECK(price > 5.99 AND price < 20.01)
);

