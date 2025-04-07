DELIMITER $$

CREATE PROCEDURE actualizar_almacen(
    IN p_id_almacen INT,
    IN p_nombre VARCHAR(255),
    IN p_direccion VARCHAR(255),
    IN p_descripcion TEXT
)
BEGIN
    UPDATE almacenes
    SET nombre = p_nombre,
        direccion = p_direccion,
        descripcion = p_descripcion
    WHERE id_almacen = p_id_almacen;
END $$

DELIMITER ;
