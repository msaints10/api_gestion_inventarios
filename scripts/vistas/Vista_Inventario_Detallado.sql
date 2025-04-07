CREATE VIEW Vista_Inventario_Detallado AS
SELECT 
    p.nombre AS Producto, 
    i.cantidad AS Stock, 
    a.nombre AS Almacén
FROM inventario i
JOIN productos p ON i.id_producto = p.id_producto
JOIN almacenes a ON i.id_almacen = a.id_almacen;
