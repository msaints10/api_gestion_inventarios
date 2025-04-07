DELIMITER //
CREATE PROCEDURE Reporte_Transacciones_Por_Fecha(IN fecha_inicio DATE, IN fecha_fin DATE)
BEGIN
    SELECT 
        t.id_transaccion, 
        t.fecha_transaccion, 
        tt.nombre_tipo AS Tipo_Transaccion, 
        et.nombre_estado AS Estado_Transaccion, 
        u.nombre AS Usuario
    FROM transacciones t
    JOIN tipos_transaccion tt ON t.id_tipo_transaccion = tt.id_tipo_transaccion
    JOIN estados_transaccion et ON t.id_estado_transaccion = et.id_estado_transaccion
    JOIN usuarios u ON t.usuario_responsable = u.id_usuario
    WHERE t.fecha_transaccion BETWEEN fecha_inicio AND fecha_fin
    ORDER BY t.fecha_transaccion DESC;
END //
DELIMITER ;
