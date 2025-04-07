DELIMITER $$
CREATE PROCEDURE actualizar_password(
    IN p_id_usuario INT,
    IN p_password VARCHAR(255)
)
BEGIN
    UPDATE usuarios
    SET password = p_password
    WHERE id_usuario = p_id_usuario;
END $$
DELIMITER ;
