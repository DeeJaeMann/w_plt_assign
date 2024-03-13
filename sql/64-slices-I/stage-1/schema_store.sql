-- Drop tables

DROP TABLE IF EXISTS stores;
DROP TABLE IF EXISTS drivers CASCADE;
DROP TABLE IF EXISTS available_pizzas CASCADE;
DROP TABLE IF EXISTS customers CASCADE;
DROP TABLE IF EXISTS available_toppings CASCADE;
DROP TABLE IF EXISTS deliveries CASCADE;
DROP TABLE IF EXISTS orders CASCADE;

-- Create tables

CREATE TABLE stores (
    id SERIAL PRIMARY KEY,
    location VARCHAR(100)   -- This csv field may need to be broken up
        NOT NULL            -- to city and country
        UNIQUE
);

-- CREATE TABLE drivers (
--     id SERIAL PRIMARY KEY,
--     store INT NOT NULL, -- ref stores.id
--     full_name VARCHAR(50)
--         NOT NULL
--         UNIQUE
--         CHECK (full_name ~ '^[A-Z][A-Za-z]* ([A-Z][A-Za-z]* ?){1,2}$')
-- );

-- CREATE TABLE available_pizzas (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(10) 
--         NOT NULL 
--         UNIQUE,
--     cost INT NOT NULL
-- );

-- CREATE TABLE customers (
--     id SERIAL PRIMARY KEY,
--     street VARCHAR(100) NOT NULL,
--     city VARCHAR(50) NOT NULL,
--     zip VARCHAR(10) NOT NULL,
--     country CHAR(2) 
--         NOT NULL
--         CHECK (country ~ '^[a-z]{2}$')
-- );

-- CREATE TABLE available_toppings (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(50) 
--         NOT NULL
--         UNIQUE
--         CHECK (name ~ '^\w+$'),
--     cost_per_pizza INT 
--         NOT NULL
--         CHECK (cost_per_pizza > 0 AND cost_per_pizza < 20)
-- );

-- CREATE TABLE deliveries (
--     id SERIAL PRIMARY KEY,
--     driver INT NOT NULL,
--     order INT NOT NULL,
--     started TIMESTAMP NOT NULL,
--     completed TIMESTAMP NOT NULL
-- );

