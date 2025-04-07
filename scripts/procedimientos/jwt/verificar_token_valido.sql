DELIMITER $$
CREATE PROCEDURE verificar_token_valido(
    IN p_id_usuario INT
)
BEGIN
    SELECT COUNT(*) > 0 AS token_valido
    FROM jwt_tokens
    WHERE id_usuario = p_id_usuario
    AND activo = 1
    AND fecha_expiracion > NOW();
END $$
DELIMITER ;