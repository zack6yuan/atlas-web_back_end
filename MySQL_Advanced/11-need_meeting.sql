-- Creates a view that lists all students that have a score under 80
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE (score < 80 AND last_meeting IS NULL);