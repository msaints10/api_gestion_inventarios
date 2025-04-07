DELIMITER $$
CREATE PROCEDURE obtener_usuario_por_nombre(
    IN p_nombre VARCHAR(255)
)
BEGIN
    SELECT id_usuario, nombre, email, activo
    FROM usuarios
    WHERE nombre = p_nombre;
END $$
DELIMITER ;
