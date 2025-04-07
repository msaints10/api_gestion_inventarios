DELIMITER $$

CREATE PROCEDURE eliminar_tipo_transaccion(
    IN p_id_tipo_transaccion INT
)
BEGIN
    DELETE FROM tipos_transaccion
    WHERE id_tipo_transaccion = p_id_tipo_transaccion;
END $$

DELIMITER ;
