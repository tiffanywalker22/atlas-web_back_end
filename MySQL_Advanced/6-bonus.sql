-- task six, add bonus
-- sql script that creates a stored procedure
DELIMITER //
CREATE PROCEDURE ADDBonus(IN user_id, in project_name VARCHAR(255), IN SCORE INT)
BEGIN
    DECLARE project_id INT;
    SELECT id INTO project_id FROM projects WHERE name = project_name;
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END //

DELIMITER ;