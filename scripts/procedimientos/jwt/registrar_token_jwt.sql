DELIMITER $$
CREATE PROCEDURE registrar_token_jwt(
    IN p_id_usuario INT,
    IN p_access_token TEXT,
    IN p_refresh_token TEXT,
    IN p_fecha_expiracion DATETIME
)
BEGIN
    INSERT INTO jwt_tokens (id_usuario, access_token, refresh_token, fecha_expiracion)
    VALUES (p_id_usuario, p_access_token, p_refresh_token, p_fecha_expiracion);
END $$
DELIMITER ;