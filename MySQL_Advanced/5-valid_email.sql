-- task five, email validation to sent
-- sql script that creates a trigger that resets attribute
DELIMITER //
CREATE TRIGGER before_email_update
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
    SET NEW.valid_email = FALSE;
    END IF;
END;
DELIMITER;
