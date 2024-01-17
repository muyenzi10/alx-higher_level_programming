-- Create database 'hbtn_0d_2 script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Cr'user_0d_2'
-- User passwoer_0d_2_pwd'
-- script should not fail
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- should have only SELECT privilege in db 'hbtn_0d_2'
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
