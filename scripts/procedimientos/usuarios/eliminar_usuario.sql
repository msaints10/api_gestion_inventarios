DELIMITER $$
CREATE PROCEDURE eliminar_usuario(
    IN p_id_usuario INT
)
BEGIN
    UPDATE usuarios SET activo = 0 WHERE id_usuario = p_id_usuario;
END $$
DELIMITER ;