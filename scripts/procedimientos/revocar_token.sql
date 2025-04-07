DELIMITER $$

CREATE PROCEDURE revocar_token(
    IN p_access_token TEXT
)
BEGIN
    UPDATE jwt_tokens
    SET activo = 0
    WHERE access_token = p_access_token;
END $$

DELIMITER ;