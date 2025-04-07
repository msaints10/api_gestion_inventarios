DELIMITER $$

CREATE PROCEDURE obtener_estado_transaccion(
    IN p_id_estado_transaccion INT
)
BEGIN
    SELECT * FROM estados_transaccion
    WHERE id_estado_transaccion = p_id_estado_transaccion;
END $$

DELIMITER ;
