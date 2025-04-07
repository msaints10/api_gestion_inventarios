DELIMITER $$
CREATE PROCEDURE activar_usuario(
    IN p_id_usuario INT
)
BEGIN
    UPDATE usuarios SET activo = 1 WHERE id_usuario = p_id_usuario;
END $$
DELIMITER ;
