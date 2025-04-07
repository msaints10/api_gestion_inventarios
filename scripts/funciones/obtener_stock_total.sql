DELIMITER $$

CREATE FUNCTION obtener_stock_total(id_producto INT) RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE total_stock INT;
    
    SELECT COALESCE(SUM(cantidad), 0) INTO total_stock
    FROM inventario
    WHERE inventario.id_producto = id_producto;
    
    RETURN total_stock;
END $$

DELIMITER ;
