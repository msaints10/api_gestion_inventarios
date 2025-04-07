DELIMITER $$

CREATE PROCEDURE asignar_rol_usuario(
    IN p_id_usuario INT,
    IN p_id_rol INT
)
BEGIN
    INSERT INTO usuarios_roles (id_usuario, id_rol)
    VALUES (p_id_usuario, p_id_rol);
END $$

DELIMITER ;
