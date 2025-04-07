DELIMITER $$

CREATE FUNCTION obtener_ultimo_precio_venta(id_producto INT) RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    DECLARE ultimo_precio DECIMAL(10,2);
    
    SELECT COALESCE(precio_unitario, 0) INTO ultimo_precio
    FROM detalle_transacciones
    WHERE id_producto = id_producto
    ORDER BY id_transaccion DESC
    LIMIT 1;
    
    RETURN ultimo_precio;
END $$

DELIMITER ;
