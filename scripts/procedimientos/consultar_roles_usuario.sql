DELIMITER $$

CREATE PROCEDURE consultar_roles_usuario(IN p_id_usuario INT)
BEGIN
    SELECT u.nombre, r.nombre_rol
    FROM usuarios_roles ur 
    JOIN usuarios u ON ur.id_usuario = u.id_usuario 
    JOIN roles r ON ur.id_rol = r.id_rol 
    WHERE u.id_usuario = p_id_usuario;
END $$

DELIMITER ;
