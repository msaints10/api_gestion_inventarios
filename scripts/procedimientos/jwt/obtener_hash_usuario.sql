DELIMITER $$
CREATE PROCEDURE obtener_hash_usuario(
    IN p_username VARCHAR(255)
)
BEGIN
    SELECT id_usuario, password FROM usuarios
    WHERE nombre = p_username AND activo = 1;
END $$
DELIMITER ;