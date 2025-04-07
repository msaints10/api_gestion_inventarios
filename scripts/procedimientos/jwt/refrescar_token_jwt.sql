DELIMITER $$
CREATE PROCEDURE refrescar_token_jwt(
    IN p_id_usuario INT,
    IN p_refresh_token TEXT,
    IN p_nuevo_access_token TEXT,
    IN p_nueva_fecha_expiracion DATETIME
)
BEGIN
    UPDATE jwt_tokens
    SET access_token = p_nuevo_access_token,
        fecha_emision = SYSDATE(),
        fecha_expiracion = p_nueva_fecha_expiracion
    WHERE id_usuario = p_id_usuario AND refresh_token = p_refresh_token AND activo = 1;
END $$
DELIMITER ;