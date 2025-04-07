DELIMITER $$
CREATE PROCEDURE obtener_usuario(
    IN p_id_usuario INT
)
BEGIN
    SELECT * FROM usuarios WHERE id_usuario = p_id_usuario;
END $$
DELIMITER ;