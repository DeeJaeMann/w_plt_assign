-- Populate inventory data
INSERT INTO inventory (id, quantity, type) VALUES (1, 100, 'Bucket of Ice Cream');
INSERT INTO inventory (id, quantity, type) VALUES (2, 100, 'Box of Cones');

-- Populate product data
INSERT INTO product (id, type) VALUES (1, 'Ice cream cone');

-- Populate task tata
INSERT INTO task (id, type) VALUES (1, 'Scoop ice cream');

-- Load employee data
\COPY employee FROM './data/employee.csv' WITH CSV HEADER;

-- Load timesheet data
\COPY timesheet FROM './data/timesheet.csv' WITH CSV HEADER;

-- Load sales data
\COPY sales FROM './data/sales.csv' WITH CSV HEADER;

-- Load mock timesheet data - this is commented out because it doesn't work
-- it is an attempt to generate data for the timesheet table

-- INSERT INTO timesheet (id, employee_id, task_id, start_time, end_time)
--     VALUES (
--         SELECT generate_series(1,10) AS id,
--         SELECT generate_series(1,10) AS employee_id, 
--         1 AS task_id,
--         SELECT generate_series(
--             TIMESTAMPTZ '2023-11-01',
--             TIMESTAMPTZ '2023-11-07',
--             INTERVAL '1 hour'
--         ) AS start_time,
--         SELECT generate_series(
--             TIMESTAMPTZ '2023-11-01',
--             TIMESTAMPTZ '2023-11-07',
--             INTERVAL '2 hours'
--         ) AS end_time);

-- WITH timesheet AS ( 
--     SELECT generate_series(1,10) AS employee_id
--     SELECT generate_series(1,10) AS employee_id,
--     SELECT generate_series(
--         TIMESTAMPTZ '2023-11-01',
--         TIMESTAMPTZ '2023-11-07',
--         INTERVAL '1 hour'
--         ) AS start_time,
-- SELECT generate_series(
--         TIMESTAMPTZ '2023-11-01',
--         TIMESTAMPTZ '2023-11-07',
--         INTERVAL '2 hours'
--         ) AS end_time
-- ) 
-- INSERT INTO timesheet (task_id, employee_id, start_time, end_time)
-- SELECT 1 AS task_id, generate_series(3,30)/3 AS employee_id, generate_series(
--         TIMESTAMPTZ '2023-11-01',
--         TIMESTAMPTZ '2023-11-07',
--         INTERVAL '1 hour'
--         ) AS start_time, now() as end_time FROM timesheet;

-- Update sequence
SELECT setval('inventory_id_seq', (SELECT MAX(id) FROM inventory));
SELECT setval('product_id_seq', (SELECT MAX(id) FROM product));
SELECT setval('task_id_seq', (SELECT MAX(id) FROM task));
SELECT setval('employee_id_seq', (SELECT MAX(id) FROM employee));
SELECT setval('timesheet_id_seq', (SELECT MAX(id) FROM timesheet));
SELECT setval('sales_id_seq', (SELECT MAX(id) FROM sales));