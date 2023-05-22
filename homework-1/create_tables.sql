-- SQL-команды для создания таблиц
CREATE TABLE customers
(id				serial	PRIMARY KEY,
 customer_id	varchar(50) NOT NULL,
 company_name	varchar(50) NOT NULL,
 contact_name   varchar(50) NOT NULL)

CREATE TABLE orders
(id				serial		PRIMARY KEY,
 order_id		int NOT NULL,
 customer_id	varchar(10) NOT NULL,
 employee_id	int NOT NULL,
 order_date		varchar(50) NOT NULL,
 ship_city		varchar(50) NOT NULL)

CREATE TABLE employees
(employee_id	serial		PRIMARY KEY,
 first_name	    varchar(50) NOT NULL,
 last_name	    varchar(50) NOT NULL,
 title          varchar(50) NOT NULL,
 birth_date		varchar(50) NOT NULL,
 notes		    text NOT NULL)

