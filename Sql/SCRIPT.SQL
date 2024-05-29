SHOW GLOBAL VARIABLES LIKE 'local_infile';
SET GLOBAL local_infile = 'ON';
SHOW GLOBAL VARIABLES LIKE 'local_infile';

USE Kaggle;

CREATE TABLE IF NOT EXISTS tbl_salarios (
    work_year INT,
    experience_level VARCHAR(25) ,
    employment_type VARCHAR(25),
    job_title VARCHAR(255),
    salary INT,
    salary_currency VARCHAR(5),
    salary_in_usd INT,
    employee_residence VARCHAR(5),
    remote_ratio INT,
    company_location VARCHAR(5),
    company_size VARCHAR(5)
);

TRUNCATE TABLE tbl_salarios;

LOAD DATA LOCAL INFILE '/Users/steve/Desktop/proyecto_parcial/python/dataset/salaries (2).csv'
INTO TABLE tbl_salarios
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES;