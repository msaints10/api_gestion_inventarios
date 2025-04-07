DELIMITER $$

CREATE PROCEDURE actualizar_estado_transaccion(
    IN p_id_estado_transaccion INT,
    IN p_nombre_estado VARCHAR(50)
)
BEGIN
    UPDATE estados_transaccion
    SET nombre_estado = p_nombre_estado
    WHERE id_estado_transaccion = p_id_estado_transaccion;
END $$

DELIMITER ;
