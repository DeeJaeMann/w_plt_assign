-- Drop tables if they exist
DROP TABLE IF EXISTS action_figure;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS game;
DROP TABLE IF EXISTS poster;

-- Add schema comment (doesn't work/not used correctly)
-- COMMENT ON SCHEMA game_review IS 'This schema contains the game store review data.';

-- Create tables
CREATE TABLE action_figure (
    id SERIAL 
        PRIMARY KEY,
    action_figure_title VARCHAR(30) 
        NOT NULL
        UNIQUE
        CHECK(action_figure_title ~ '^[A-Z][a-z]*(?:(?: |-)[A-Z\d][a-z]*)*$'),
    quantity INT
        NOT NULL
        CHECK(quantity > 0 AND quantity < 31),
    price DECIMAL(4,2)
        NOT NULL
        CHECK(price BETWEEN 10 AND 100)
);

COMMENT ON TABLE action_figure IS 'This table contains the action figure data.';

CREATE TABLE employee (
    id SERIAL 
        PRIMARY KEY,
    employee_name VARCHAR(30)
        NOT NULL
        CHECK(employee_name ~ '^[A-Z][a-z]*(?: [A-Z][a-z]*)$'),
    position VARCHAR(50)
        NOT NULL,
        CHECK(position IN (
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
        CHECK(salary BETWEEN 31987.20 AND 65000)
);

COMMENT ON TABLE employee IS 'This table contains the employee data.';

CREATE TABLE game (
    game_id SERIAL
        PRIMARY KEY,
    game_title VARCHAR(255)
        NOT NULL
        UNIQUE
        -- Theres more missing from this: The Witcher 3: Wild Hunt -> fails, break down and figure out why
        -- CHECK(game_title ~ '^[A-Z\d][A-Za-z\d](?:(?: |:)[\dA-Z](?:\:|[\dA-Za-z]*):?)*$'),

    quantity INT
        NOT NULL,
    price DECIMAL(4,2)
        NOT NULL
);

COMMENT ON TABLE game IS 'This table contains the game data.';

CREATE TABLE poster (
    id SERIAL
        PRIMARY KEY,
    poster_title VARCHAR(30)
        NOT NULL
        UNIQUE,
    quantity INT
        NOT NULL,
    price DECIMAL(4,2)
        NOT NULL
);

COMMENT ON TABLE poster IS 'This table contains the poster data.';