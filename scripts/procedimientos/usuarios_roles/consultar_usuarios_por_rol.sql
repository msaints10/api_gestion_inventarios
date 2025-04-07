DELIMITER $$
CREATE PROCEDURE consultar_usuarios_por_rol(
    IN p_id_rol INT
)
BEGIN
    SELECT u.id_usuario, u.nombre, u.email
    FROM usuarios u
    INNER JOIN usuarios_roles ur ON u.id_usuario = ur.id_usuario
    WHERE ur.id_rol = p_id_rol;
END $$
DELIMITER ;