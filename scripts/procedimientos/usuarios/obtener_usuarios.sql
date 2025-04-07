DELIMITER $$
CREATE PROCEDURE obtener_usuarios(
    IN p_activo BOOLEAN
)
BEGIN
    IF p_activo IS NULL THEN
        SELECT * FROM usuarios;
    ELSE
        SELECT * FROM usuarios WHERE activo = p_activo;
    END IF;
END $$
DELIMITER ;