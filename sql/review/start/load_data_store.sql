-- Insert sample data from .csv files into tables
\COPY action_figure FROM './data/action_figure.csv' WITH CSV HEADER;
\COPY employee FROM './data/employee.csv' WITH CSV HEADER;
\COPY game FROM './data/game.csv' WITH CSV HEADER;
\COPY poster FROM './data/poster.csv' WITH CSV HEADER;

-- Update serialized tables for keys
SELECT setval('action_figure_id_seq', (SELECT MAX(id) FROM action_figure));
SELECT setval('employee_id_seq', (SELECT MAX(id) FROM employee));
SELECT setval('game_game_id_seq', (SELECT MAX(game_id) FROM game));
SELECT setval('poster_id_seq', (SELECT MAX(id) FROM poster));