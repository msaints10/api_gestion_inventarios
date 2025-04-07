DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `obtener_rol`(
    IN p_id_rol INT
)
BEGIN
	SELECT id_rol, nombre_rol, descripcion FROM roles
    WHERE id_rol = p_id_rol;
END$$
DELIMITER ;
