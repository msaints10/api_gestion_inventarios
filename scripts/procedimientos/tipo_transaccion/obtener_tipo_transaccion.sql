DELIMITER $$

CREATE PROCEDURE obtener_tipo_transaccion(
    IN p_id_tipo_transaccion INT
)
BEGIN
    SELECT * FROM tipos_transaccion
    WHERE id_tipo_transaccion = p_id_tipo_transaccion;
END $$

DELIMITER ;
