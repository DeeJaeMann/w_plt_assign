-- 1 Query names of all gaming engines

SELECT engine_name FROM gaming_engine;

-- 2 Query total games in stock

SELECT SUM(quantity) FROM game;

-- 3 Query titles of all games with price greater than $30.00

SELECT game_title FROM game
    WHERE price > 30.00;

-- 4 Query titles and quantities of games with less than 20 in stock

SELECT game_title, quantity FROM game
    WHERE quantity < 20;

-- 5 Query total number of grenre-game associations

SELECT COUNT(id) FROM genre_game;

-- 6 Query titles of action figures with price between 20.00 and 50.00

SELECT action_figure_title FROM action_figure
    WHERE price > 19.99 AND price < 50.01;

-- 7 Query poster title and prices with quantities between 15 and 30

SELECT poster_title, price FROM poster
    WHERE price > 14.99 AND price < 30.01;

-- 8 Query 