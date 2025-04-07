DELIMITER $$

CREATE PROCEDURE eliminar_estado_transaccion(
    IN p_id_estado_transaccion INT
)
BEGIN
    DELETE FROM estados_transaccion
    WHERE id_estado_transaccion = p_id_estado_transaccion;
END $$

DELIMITER ;
