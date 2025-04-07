DELIMITER $$
CREATE PROCEDURE reporte_ventas_por_producto(
    IN p_id_producto INT
)
BEGIN
    SELECT dt.id_producto, p.nombre, SUM(dt.cantidad) AS total_vendido, SUM(dt.subtotal) AS ingreso_total
    FROM detalle_transacciones dt
    JOIN transacciones t ON dt.id_transaccion = t.id_transaccion
    JOIN productos p ON dt.id_producto = p.id_producto
    JOIN tipos_transaccion tt ON t.id_tipo_transaccion = tt.id_tipo_transaccion
    WHERE tt.nombre_tipo = 'venta' AND dt.id_producto = p_id_producto
    GROUP BY dt.id_producto;
END $$
DELIMITER ;