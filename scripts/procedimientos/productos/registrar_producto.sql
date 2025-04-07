DELIMITER $$

CREATE PROCEDURE registrar_producto(
    IN p_codigo VARCHAR(50),
    IN p_nombre VARCHAR(255),
    IN p_descripcion TEXT,
    IN p_precio_unitario DECIMAL(10,2),
    IN p_stock_total INT
)
BEGIN
    INSERT INTO productos (
        codigo,
        nombre,
        descripcion,
        precio_unitario,
        stock_total,
        fecha_creacion
    )
    VALUES (
        p_codigo,
        p_nombre,
        p_descripcion,
        p_precio_unitario,
        p_stock_total,
        SYSDATE()
    );
END $$

DELIMITER ;
