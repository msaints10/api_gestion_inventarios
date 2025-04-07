SELECT p.nombre, a_origen.nombre AS almacén_origen, a_destino.nombre AS almacén_destino, dt.cantidad
FROM detalle_transacciones dt
JOIN productos p ON dt.id_producto = p.id_producto
JOIN almacenes a_origen ON dt.id_almacen_origen = a_origen.id_almacen
JOIN almacenes a_destino ON dt.id_almacen_destino = a_destino.id_almacen
WHERE dt.id_almacen_destino IS NOT NULL
ORDER BY a_origen.nombre, a_destino.nombre;