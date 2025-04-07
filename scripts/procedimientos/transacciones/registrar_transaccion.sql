DELIMITER $$
CREATE PROCEDURE registrar_transaccion(
    IN p_id_tipo_transaccion INT,
    IN p_usuario_responsable INT,
    IN p_id_almacen_origen INT,
    IN p_id_almacen_destino INT,
    IN p_total_transaccion DECIMAL(10,2),
    IN p_id_estado_transaccion INT,
    IN p_nota TEXT
)
BEGIN
    INSERT INTO transacciones (
        id_tipo_transaccion,
        usuario_responsable,
        id_almacen_origen,
        id_almacen_destino,
        total_transaccion,
        id_estado_transaccion,
        nota,
        fecha_transaccion
    )
    VALUES (
        p_id_tipo_transaccion,
        p_usuario_responsable,
        p_id_almacen_origen,
        p_id_almacen_destino,
        p_total_transaccion,
        p_id_estado_transaccion,
        p_nota,
        SYSDATE()
    );
END $$
DELIMITER ;