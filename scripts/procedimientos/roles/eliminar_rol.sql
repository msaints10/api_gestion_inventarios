DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `eliminar_rol`(
    IN p_id_rol INT
)
BEGIN
	DELETE FROM roles
    WHERE id_rol = p_id_rol;
END$$
DELIMITER ;
