DELIMITER $$

CREATE PROCEDURE eliminar_rol_usuario(
    IN p_id_usuario INT,
    IN p_id_rol INT
)
BEGIN
    DELETE FROM usuarios_roles
    WHERE id_usuario = p_id_usuario AND id_rol = p_id_rol;
END $$

DELIMITER ;
