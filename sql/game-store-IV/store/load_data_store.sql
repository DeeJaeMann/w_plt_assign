-- Insert Sample Data into Game Table
\COPY poster FROM './data/poster.csv' WITH CSV HEADER;
\COPY action_figure FROM './data/action_figure.csv' WITH CSV HEADER;
\COPY gaming_engine FROM './data/gaming_engine.csv' WITH CSV HEADER;
\COPY genre FROM './data/genre.csv' WITH CSV HEADER;
\COPY game FROM './data/game.csv' WITH CSV HEADER;
\COPY genre_game FROM './data/genre_game.csv' WITH CSV HEADER;
\COPY employee FROM './data/employee.csv' WITH CSV HEADER;
\COPY social_security FROM './data/social_security.csv' WITH CSV HEADER;
\COPY shifts FROM './data/shifts.csv' WITH CSV HEADER;

SELECT setval('poster_id_seq', (SELECT MAX(id) FROM poster));
SELECT setval('action_figure_id_seq', (SELECT MAX(id) FROM action_figure));
SELECT setval('gaming_engine_id_seq', (SELECT MAX(id) FROM gaming_engine));
SELECT setval('genre_id_seq', (SELECT MAX(id) FROM genre));
SELECT setval('game_id_seq', (SELECT MAX(id) FROM game));
SELECT setval('genre_game_id_seq', (SELECT MAX(id) FROM genre_game));
SELECT setval('employee_id_seq', (SELECT MAX(id) FROM employee));
SELECT setval('social_security_id_seq', (SELECT MAX(id) FROM social_security));
SELECT setval('shifts_id_seq', (SELECT MAX(id) FROM shifts));