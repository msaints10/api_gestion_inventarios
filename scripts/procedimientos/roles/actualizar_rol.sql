DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `actualizar_rol`(
    IN p_id_rol INT,
    IN p_nombre_rol VARCHAR(100),
    IN p_descripcion TEXT
)
BEGIN
	UPDATE roles
    set nombre_rol = p_nombre_rol, descripcion = p_descripcion
    WHERE id_rol = p_id_rol;
END$$
DELIMITER ;
