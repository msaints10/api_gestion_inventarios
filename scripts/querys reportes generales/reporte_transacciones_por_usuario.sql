SELECT t.id_transaccion, t.fecha_transaccion, tt.nombre_tipo, et.nombre_estado, u.nombre
FROM transacciones t
JOIN tipos_transaccion tt ON t.id_tipo_transaccion = tt.id_tipo_transaccion
JOIN estados_transaccion et ON t.id_estado_transaccion = et.id_estado_transaccion
JOIN usuarios u ON t.usuario_responsable = u.id_usuario
ORDER BY t.fecha_transaccion DESC;