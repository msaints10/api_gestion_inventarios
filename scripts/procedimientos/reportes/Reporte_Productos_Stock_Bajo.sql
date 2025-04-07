DELIMITER //
CREATE PROCEDURE Reporte_Productos_Stock_Bajo(IN stock_minimo INT)
BEGIN
    SELECT 
        p.nombre AS Producto, 
        SUM(i.cantidad) AS Stock_Total
    FROM inventario i
    JOIN productos p ON i.id_producto = p.id_producto
    GROUP BY p.nombre
    HAVING SUM(i.cantidad) < stock_minimo
    ORDER BY p.nombre;
END //
DELIMITER ;
