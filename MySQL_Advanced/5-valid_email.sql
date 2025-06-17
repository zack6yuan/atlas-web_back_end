-- Creates a trigger that resets the attribute valid_email
-- Only when the email has been changed
DELIMETER //
CREATE TRIGGER reset_email BEFORE INSERT ON email
FOR EACH ROW
BEGIN
    SET valid_email = NULL
END;//
DELIMETER ;