DELIMITER $$
CREATE PROCEDURE revocar_token(
    IN p_id_usuario INT
)
BEGIN
    UPDATE jwt_tokens
    SET activo = 0
    WHERE id_usuario = p_id_usuario;
END $$
DELIMITER ;