-- Load data

INSERT INTO student (id, first_name, last_name, age, grade) VALUES (1, 'John', 'Doe', 18, 'A');
INSERT INTO student (id, first_name, last_name, age, grade) VALUES (2, 'Jame', 'Smith', 19, 'B');
INSERT INTO student (id, first_name, last_name, age, grade) VALUES (3, 'Bob', 'Johnson', 20, 'C');
INSERT INTO student (id, first_name, last_name, age, grade) VALUES (4, 'Emily', 'Williams', 18, 'A');
INSERT INTO student (id, first_name, last_name, age, grade) VALUES (5, 'Michael', 'Brown', 19, 'B');
INSERT INTO student (id, first_name, last_name, age, grade) VALUES (6, 'Samantha', 'Davis', 22, 'A');
INSERT INTO student (id, first_name, last_name, age, grade) VALUES (7, 'Oliver', 'Jones', 20, 'B');
INSERT INTO student (id, first_name, last_name, age, grade) VALUES (8, 'Sophia', 'Miller', 21, 'A');
INSERT INTO student (id, first_name, last_name, age, grade) VALUES (9, 'Ethan', 'Wilson', 19, 'C');
INSERT INTO student (id, first_name, last_name, age, grade) VALUES (10, 'Isabella', 'Moore', 22, 'B');

SELECT setval('students_id_seq', (SELECT MAX(id) FROM students));