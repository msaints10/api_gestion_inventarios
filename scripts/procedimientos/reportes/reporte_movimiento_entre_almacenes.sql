DELIMITER $$
CREATE PROCEDURE reporte_movimiento_entre_almacenes(
    IN p_id_almacen_origen INT,
    IN p_id_almacen_destino INT
)
BEGIN
    SELECT t.id_transaccion, p.nombre AS producto, dt.cantidad, t.fecha_transaccion
    FROM detalle_transacciones dt
    JOIN transacciones t ON dt.id_transaccion = t.id_transaccion
    JOIN productos p ON dt.id_producto = p.id_producto
    WHERE dt.id_almacen_origen = p_id_almacen_origen AND dt.id_almacen_destino = p_id_almacen_destino;
END $$
DELIMITER ;
