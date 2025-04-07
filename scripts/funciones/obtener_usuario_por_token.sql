DELIMITER $$

CREATE FUNCTION obtener_usuario_por_token(p_token TEXT) RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE usuario INT;

    SELECT id_usuario INTO usuario
    FROM jwt_tokens
    WHERE access_token = p_token
    AND activo = 1
    LIMIT 1;

    RETURN usuario;
END $$

DELIMITER ;