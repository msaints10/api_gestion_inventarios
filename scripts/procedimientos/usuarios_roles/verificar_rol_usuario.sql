DELIMITER $$
CREATE PROCEDURE verificar_rol_usuario(
    IN p_id_usuario INT,
    IN p_id_rol INT
)
BEGIN
    IF EXISTS (
        SELECT 1 FROM usuarios_roles
        WHERE id_usuario = p_id_usuario AND id_rol = p_id_rol
    ) THEN
        SELECT 1 AS tiene_rol;
    ELSE
        SELECT 0 AS tiene_rol;
    END IF;
END $$
DELIMITER ;
