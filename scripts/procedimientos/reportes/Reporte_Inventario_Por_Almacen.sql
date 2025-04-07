DELIMITER //
CREATE PROCEDURE Reporte_Inventario_Por_Almacen(IN id_almacen_param INT)
BEGIN
    SELECT 
        p.nombre AS Producto, 
        i.cantidad AS Stock, 
        a.nombre AS Almacén
    FROM inventario i
    JOIN productos p ON i.id_producto = p.id_producto
    JOIN almacenes a ON i.id_almacen = a.id_almacen
    WHERE a.id_almacen = id_almacen_param
    ORDER BY p.nombre;
END //
DELIMITER ;
