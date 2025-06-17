-- Creates a view that lists all students that have a score under 80
CREATE VIEW need_meeting AS
SELECT score
FROM students
WHERE score < 80