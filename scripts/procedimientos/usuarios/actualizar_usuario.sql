DELIMITER $$
CREATE PROCEDURE actualizar_usuario(
    IN p_id_usuario INT,
    IN p_nombre VARCHAR(255),
    IN p_email VARCHAR(255)
)
BEGIN
    UPDATE usuarios
    SET nombre = p_nombre,
        email = p_email
    WHERE id_usuario = p_id_usuario;
END $$
DELIMITER ;