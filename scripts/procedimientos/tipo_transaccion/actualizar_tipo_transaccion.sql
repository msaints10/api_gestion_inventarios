DELIMITER $$

CREATE PROCEDURE actualizar_tipo_transaccion(
    IN p_id_tipo_transaccion INT,
    IN p_nombre_tipo VARCHAR(100),
    IN p_afecta_stock BOOLEAN
)
BEGIN
    UPDATE tipos_transaccion
    SET nombre_tipo = p_nombre_tipo,
        afecta_stock = p_afecta_stock
    WHERE id_tipo_transaccion = p_id_tipo_transaccion;
END $$

DELIMITER ;
