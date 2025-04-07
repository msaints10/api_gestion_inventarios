DELIMITER $$
CREATE PROCEDURE reporte_productos_stocktotal_por_almacen(
    IN p_id_almacen INT
)
BEGIN
    SELECT p.id_producto, p.nombre, i.cantidad, a.nombre AS nombre_almacen
    FROM productos p
    JOIN inventario i ON p.id_producto = i.id_producto
    JOIN almacenes a ON i.id_almacen = a.id_almacen
    WHERE a.id_almacen = p_id_almacen;
END $$
DELIMITER ;