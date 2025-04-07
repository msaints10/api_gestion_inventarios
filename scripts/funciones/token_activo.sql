DELIMITER $$

CREATE FUNCTION token_activo(p_token TEXT) RETURNS BOOLEAN
DETERMINISTIC
BEGIN
    DECLARE es_activo BOOLEAN;

    SELECT EXISTS(
        SELECT 1
        FROM jwt_tokens
        WHERE access_token = p_token
        AND activo = 1
        AND (fecha_expiracion IS NULL OR fecha_expiracion > NOW())
    ) INTO es_activo;

    RETURN es_activo;
END $$

DELIMITER ;