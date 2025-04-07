DELIMITER $$
CREATE PROCEDURE actualizar_detalle_transaccion(
    IN p_id_detalle INT,
    IN p_id_transaccion INT,
    IN p_id_producto INT,
    IN p_cantidad INT,
    IN p_precio_unitario DECIMAL(10,2),
    IN p_subtotal DECIMAL(10,2),
    IN p_id_almacen_origen INT,
    IN p_id_almacen_destino INT
)
BEGIN
    UPDATE detalle_transacciones
    SET id_transaccion = p_id_transaccion,
        id_producto = p_id_producto,
        cantidad = p_cantidad,
        precio_unitario = p_precio_unitario,
        subtotal = p_subtotal,
        id_almacen_origen = p_id_almacen_origen,
        id_almacen_destino = p_id_almacen_destino
    WHERE id_detalle = p_id_detalle;
END $$
DELIMITER ;