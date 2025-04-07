DELIMITER $$

CREATE PROCEDURE registrar_almacen(
    IN p_nombre VARCHAR(255),
    IN p_direccion VARCHAR(255),
    IN p_descripcion TEXT
)
BEGIN
    INSERT INTO almacenes (nombre, direccion, descripcion, fecha_creacion)
    VALUES (p_nombre, p_direccion, p_descripcion, SYSDATE());
END $$

DELIMITER ;
