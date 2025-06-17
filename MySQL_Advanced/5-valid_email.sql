-- Creates a trigger that resets the attribute valid_email
-- Only when the email has been changed
DELIMITER //
CREATE TRIGGER reset_email BEFORE INSERT ON email
FOR EACH ROW
BEGIN
    SET NEW.valid_email = NULL;
END;//
DELIMITER ;