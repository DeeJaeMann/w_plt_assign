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
        UNIQUE,
    quantity INT
        NOT NULL,
    price DECIMAL(4,2)
        NOT NULL
);

COMMENT ON TABLE action_figure IS 'This table contains the action figure data.';

CREATE TABLE employee (
    id SERIAL 
        PRIMARY KEY,
    employee_name VARCHAR(30)
        NOT NULL,
    position VARCHAR
        NOT NULL,
    salary DECIMAL(7,2)
        NOT NULL
);

COMMENT ON TABLE employee IS 'This table contains the employee data.';

CREATE TABLE game (
    game_id SERIAL
        PRIMARY KEY,
    game_title VARCHAR(30)
        NOT NULL
        UNIQUE,
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