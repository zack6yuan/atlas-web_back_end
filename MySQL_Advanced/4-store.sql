-- Creates a trigger that decreases the quantity of an item after adding a new order
DELIMITER //
CREATE TRIGGER decreaser AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE quantity
    SET quantity = quantity - number;
END;//
DELIMITER ;