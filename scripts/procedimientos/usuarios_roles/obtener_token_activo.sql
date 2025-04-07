DELIMITER $$
CREATE PROCEDURE obtener_token_activo(
    IN p_id_usuario INT
)
BEGIN
    SELECT * FROM jwt_tokens
    WHERE id_usuario = p_id_usuario AND activo = 1
    ORDER BY fecha_emision DESC
    LIMIT 1;
END $$
DELIMITER ;