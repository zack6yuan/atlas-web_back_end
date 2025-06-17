-- Creates a function SafeDiv
DELIMITER // -- set delimiter so function does not end with semicolons
CREATE FUNCTION SafeDiv(
    a INT,
    b INT
)
RETURNS FLOAT
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END //

DELIMITER ; -- set the delimiter back to the semicolon
