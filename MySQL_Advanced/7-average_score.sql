-- Creates a stored procesure that computes and stores the average score for a student
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    INSERT INTO
        score
    SELECT
        AVG(score)
    FROM
        corrections
    WHERE
        user_id = user_id;
END //
DELIMITER ;