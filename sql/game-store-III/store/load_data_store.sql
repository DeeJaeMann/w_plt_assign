-- Insert Sample Data into Game Table
\COPY game FROM './data/game.csv' WITH CSV HEADER;
\COPY action_figure FROM './data/action_figure.csv' WITH CSV HEADER;
\COPY employee FROM './data/employee.csv' WITH CSV HEADER;
\COPY poster FROM './data/poster.csv' WITH CSV HEADER;