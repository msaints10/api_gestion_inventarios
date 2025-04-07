SELECT p.nombre, a.nombre AS almacén, i.cantidad
FROM inventario i
JOIN productos p ON i.id_producto = p.id_producto
JOIN almacenes a ON i.id_almacen = a.id_almacen
ORDER BY p.nombre, a.nombre;