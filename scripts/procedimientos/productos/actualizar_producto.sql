DELIMITER $$

CREATE PROCEDURE actualizar_producto(
    IN p_id_producto INT,
    IN p_codigo VARCHAR(50),
    IN p_nombre VARCHAR(255),
    IN p_descripcion TEXT,
    IN p_precio_unitario DECIMAL(10,2),
    IN p_stock_total INT
)
BEGIN
    UPDATE productos
    SET
        codigo = p_codigo,
        nombre = p_nombre,
        descripcion = p_descripcion,
        precio_unitario = p_precio_unitario,
        stock_total = p_stock_total,
        fecha_modificacion = SYSDATE()
    WHERE id_producto = p_id_producto;
END $$

DELIMITER ;
