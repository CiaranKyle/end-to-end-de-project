\c de_project

ALTER TABLE customers
    ADD FullName VARCHAR(256);

UPDATE customers
set FullName = concat(first_name, ' ', last_name);
