-- Drop the table if it exists
DROP TABLE IF EXISTS game CASCADE;
DROP TABLE IF EXISTS genre CASCADE;
DROP TABLE IF EXISTS gaming_engine CASCADE;
DROP TABLE IF EXISTS genre_game CASCADE;
DROP TABLE IF EXISTS poster;
DROP TABLE IF EXISTS action_figure;
DROP TABLE IF EXISTS employee CASCADE;
DROP TABLE IF EXISTS social_security CASCADE;
DROP TABLE IF EXISTS shifts CASCADE;


-- Create Tables
CREATE TABLE action_figure (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50) 
        UNIQUE 
        NOT NULL 
        CHECK(title ~ '^[A-Z0-9][\w\s\-]*$'),
    quantity INT 
        NOT NULL 
        CHECK(quantity > 0 AND quantity < 31),
    price DECIMAL(5,2) 
        NOT NULL 
        CHECK(price > 9.99 AND price < 100.01)
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

CREATE TABLE gaming_engine (
    id SERIAL PRIMARY KEY,
    engine VARCHAR(30) 
        NOT NULL 
        UNIQUE
        CHECK(engine ~ '^[A-Z0-9][\w \-:''\\]+$')
);

CREATE TABLE game (
    id SERIAL PRIMARY KEY,
    engine INT NOT NULL, -- ref gaming_engine.id
    title VARCHAR(50) 
        UNIQUE 
        NOT NULL 
        CHECK (title ~ '^[A-Z0-9][\w \-:''\\]+$'),
    quantity INT 
        NOT NULL 
        CHECK(quantity > 0 AND quantity < 51),
    price DECIMAL(5, 2) 
        NOT NULL 
        CHECK(price > 9.99 AND price < 60.01),
    FOREIGN KEY (engine)
        REFERENCES gaming_engine(id)
);

CREATE TABLE genre (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20)
        NOT NULL
        UNIQUE
        CHECK(name ~ '^[A-Z0-9][\w \-:''\\]+$')
);

CREATE TABLE genre_game (
    id SERIAL PRIMARY KEY,
    game INT NOT NULL, -- ref game.id
    genre INT NOT NULL, -- ref genre.id
    FOREIGN KEY (game)
        REFERENCES game(id),
    FOREIGN KEY (genre)
        REFERENCES genre(id)
);

CREATE TABLE employee (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) 
        NOT NULL 
        -- This ensures the first and last names are capitalized
        -- It also allows for an optional middle name that must be capitalized
        CHECK(name ~ '^([A-Z][A-Za-z]*) ([A-Z][A-Za-z]*\s?){1,2}$'),
    position VARCHAR(50) 
        NOT NULL 
        -- This is sloppy and should come from a table
        -- RegEx method
        -- CHECK(
        --     position ~ '^Sales Associate|Store Manager|Inventory Clerk|Customer Service Representative|IT Specialist|Marketing Coordinator|Assistant Manager|Finance Analyst|Security Officer|HR Coordinator$'), -- match the words from the description
        CHECK( position IN (
            'Sales Associate',
            'Store Manager',
            'Inventory Clerk',
            'Customer Service Representative',
            'IT Specialist',
            'Marketing Coordinator',
            'Assistant Manager',
            'Finance Analyst',
            'Security Officer',
            'HR Coordinator'
        )),
    salary DECIMAL(7,2)
        NOT NULL
        CHECK(salary > 31999.99 AND salary < 65000.01)
    -- 31987.19 is 15.37/hr
    -- 32000 is 15.38/hr
    -- 16.66 ~ 34652.80  one record set to 32000
    -- 31.25 ~ 65000.00
);

CREATE TABLE social_security (
    id SERIAL PRIMARY KEY,
    employee INT NOT NULL,  -- ref employee.id
    ssn VARCHAR(11)  
        NOT NULL
        UNIQUE
        CHECK(ssn ~ '^\d{3}\-\d{2}\-\d{4}$'), 
    FOREIGN KEY (employee)
        REFERENCES employee(id)
);

CREATE TABLE shifts (
    id SERIAL PRIMARY KEY,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    employee INT NOT NULL,  -- ref employee.id
    FOREIGN KEY (employee)
        REFERENCES employee(id)
);


