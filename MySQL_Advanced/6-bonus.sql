-- Creates a stored procedure AddBonus that adds a new correction for a student
DELIMITER //
CREATE PROCEDURE AddBonus(
    IN user_id INT,
    IN project_name VARCHAR(100),
    IN score INT
)
BEGIN
    INSERT INTO corrections(
        user_id, project_id, score
    );
END;
DELIMITER ;  