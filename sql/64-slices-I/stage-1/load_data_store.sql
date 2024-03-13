-- Load the data
\COPY stores FROM './data/stores.csv' WITH CSV HEADER;

-- Update the sequence table
SELECT setval('stores_id_seq', (SELECT MAX(id) FROM stores));