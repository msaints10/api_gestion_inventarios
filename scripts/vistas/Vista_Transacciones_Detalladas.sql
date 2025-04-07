CREATE VIEW Vista_Transacciones_Detalladas AS
SELECT 
    t.id_transaccion, 
    t.fecha_transaccion, 
    tt.nombre_tipo AS Tipo_Transaccion, 
    et.nombre_estado AS Estado_Transaccion, 
    u.nombre AS Usuario
FROM transacciones t
JOIN tipos_transaccion tt ON t.id_tipo_transaccion = tt.id_tipo_transaccion
JOIN estados_transaccion et ON t.id_estado_transaccion = et.id_estado_transaccion
JOIN usuarios u ON t.usuario_responsable = u.id_usuario;
