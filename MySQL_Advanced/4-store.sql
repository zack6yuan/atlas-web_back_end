-- Creates a trigger that decreases the quantity of an item after adding a new order
DELIMITER //
CREATE TRIGGER decreaser AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    SET items = items - quantity;
END;//
DELIMITER ;