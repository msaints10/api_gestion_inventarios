DELIMITER $$

CREATE TRIGGER validar_stock
BEFORE INSERT ON detalle_transacciones
FOR EACH ROW
BEGIN
    DECLARE stock_disponible INT DEFAULT 0;

    -- Obtener la cantidad disponible del inventario
    SELECT cantidad INTO stock_disponible
    FROM inventario
    WHERE id_producto = NEW.id_producto AND id_almacen = NEW.id_almacen_origen
    LIMIT 1;

    -- Verificar si hay suficiente stock
    IF stock_disponible < NEW.cantidad THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No hay suficiente stock en el almacén.';
    END IF;
END $$

DELIMITER ;

