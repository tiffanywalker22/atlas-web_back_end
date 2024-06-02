-- task five, email validation to sent
-- sql script that creates a trigger that resets attribute
CREATE TRIGGER before_email_update
BEFORE UPDATE ON users
FOR EACH ROW
IF OLD.email <> NEW.email THEN
SET NEW.valid_email = FALSE;
END IF;
