-- Load data

COPY student(id, first_name, last_name, age, subject)
FROM '/home/deemann/vscode-workspace/CodePlatoon/w_plt_assign/flask/flask_postgres_school/data/student.csv'
DELIMITER ','
CSV HEADER;

COPY teachers(id, first_name, last_name, age, subject)
FROM '/home/deemann/vscode-workspace/CodePlatoon/w_plt_assign/flask/flask_postgres_school/data/teachers.csv'
DELIMITER ','
CSV HEADER;

COPY student(id, subject)
FROM '/home/deemann/vscode-workspace/CodePlatoon/w_plt_assign/flask/flask_postgres_school/data/subjects.csv'
DELIMITER ','
CSV HEADER;

SELECT setval('student_id_seq', (SELECT MAX(id) FROM student));
SELECT setval('teachers_id_seq', (SELECT MAX(id) FROM teachers));
SELECT setval('subjects_id_seq', (SELECT MAX(id) FROM subjects));