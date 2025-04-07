DELIMITER $$

CREATE FUNCTION obtener_valor_total_inventario() RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    DECLARE valor_total DECIMAL(10,2);
    
    SELECT COALESCE(SUM(i.cantidad * p.precio_unitario), 0) INTO valor_total
    FROM inventario i
    JOIN productos p ON i.id_producto = p.id_producto;
    
    RETURN valor_total;
END $$

DELIMITER ;
