DELIMITER $$

CREATE PROCEDURE registrar_rol(
    IN p_nombre_rol VARCHAR(100),
    IN p_descripcion TEXT
)
BEGIN
    INSERT INTO roles (nombre_rol, descripcion)
    VALUES (p_nombre_rol, p_descripcion);
END $$

DELIMITER ;
