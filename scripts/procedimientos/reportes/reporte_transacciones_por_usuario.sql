DELIMITER $$
CREATE PROCEDURE reporte_transacciones_por_usuario(
    IN p_id_usuario INT
)
BEGIN
    SELECT t.id_transaccion, tt.nombre_tipo, t.total_transaccion, t.fecha_transaccion
    FROM transacciones t
    JOIN tipos_transaccion tt ON t.id_tipo_transaccion = tt.id_tipo_transaccion
    WHERE t.usuario_responsable = p_id_usuario
    ORDER BY t.fecha_transaccion DESC;
END $$
DELIMITER ;