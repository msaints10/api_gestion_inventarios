DELIMITER $$
CREATE PROCEDURE obtener_usuario_por_id(
    IN p_id_usuario INT
)
BEGIN
    SELECT id_usuario, nombre, email, activo
    FROM usuarios
    WHERE id_usuario = p_id_usuario;
END $$
DELIMITER ;