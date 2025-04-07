DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `obtener_roles`()
BEGIN
	SELECT id_rol, nombre_rol, descripcion FROM roles;
END$$
DELIMITER ;
