-- This SQL command queries the information_schema to get the full description of the table.

SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT, EXTRA
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = '<database_name>' AND TABLE_NAME = 'first_table';
