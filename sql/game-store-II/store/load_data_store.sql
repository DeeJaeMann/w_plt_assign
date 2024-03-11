-- Load data from csv into game_store tables

\COPY game FROM './data/game.csv' WITH CSV HEADER;
\COPY action_figure FROM './data/action_figure.csv' WITH CSV HEADER;
\COPY poster FROM './data/poster.csv' WITH CSV HEADER;
\COPY employee FROM './data/employee.csv' WITH CSV HEADER;

SELECT setval('game_game_id_seq', (SELECT MAX(game_id) FROM game));
SELECT setval('action_figure_action_figure_id_seq', (SELECT MAX(action_figure_id) FROM action_figure));
SELECT setval('poster_poster_id_seq', (SELECT MAX(poster_id) FROM poster));
SELECT setval('employee_employee_id_seq', (SELECT MAX(employee_id) FROM employee));