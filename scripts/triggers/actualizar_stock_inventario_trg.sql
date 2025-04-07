DELIMITER $$

CREATE TRIGGER actualizar_stock
AFTER INSERT ON detalle_transacciones
FOR EACH ROW
BEGIN
    -- Reducir stock en el almacén de origen
    UPDATE inventario
    SET cantidad = cantidad - NEW.cantidad
    WHERE id_producto = NEW.id_producto AND id_almacen = NEW.id_almacen_origen;

    -- Si hay un almacén de destino (traslado), incrementar el stock en destino
    IF NEW.id_almacen_destino IS NOT NULL THEN
        INSERT INTO inventario (id_producto, id_almacen, cantidad)
        VALUES (NEW.id_producto, NEW.id_almacen_destino, NEW.cantidad)
        ON DUPLICATE KEY UPDATE cantidad = cantidad + NEW.cantidad;
    END IF;
END $$

DELIMITER ;
