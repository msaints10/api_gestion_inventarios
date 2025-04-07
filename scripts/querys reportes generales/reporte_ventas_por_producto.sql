SELECT p.nombre, SUM(dt.cantidad) AS total_vendido, SUM(dt.subtotal) AS total_ingresos
FROM detalle_transacciones dt
JOIN productos p ON dt.id_producto = p.id_producto
JOIN transacciones t ON dt.id_transaccion = t.id_transaccion
WHERE t.id_tipo_transaccion = 1
GROUP BY p.id_producto
ORDER BY total_vendido DESC;