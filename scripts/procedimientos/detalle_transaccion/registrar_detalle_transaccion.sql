DELIMITER $$
CREATE PROCEDURE registrar_detalle_transaccion(
    IN p_id_transaccion INT,
    IN p_id_producto INT,
    IN p_cantidad INT,
    IN p_precio_unitario DECIMAL(10,2),
    IN p_subtotal DECIMAL(10,2),
    IN p_id_almacen_origen INT,
    IN p_id_almacen_destino INT
)
BEGIN
    INSERT INTO detalle_transacciones (
        id_transaccion,
        id_producto,
        cantidad,
        precio_unitario,
        subtotal,
        id_almacen_origen,
        id_almacen_destino
    )
    VALUES (
        p_id_transaccion,
        p_id_producto,
        p_cantidad,
        p_precio_unitario,
        p_subtotal,
        p_id_almacen_origen,
        p_id_almacen_destino
    );
END $$
DELIMITER ;