DELIMITER $$
CREATE PROCEDURE eliminar_transaccion(
    IN p_id_transaccion INT
)
BEGIN
    DELETE FROM transacciones WHERE id_transaccion = p_id_transaccion;
END $$
DELIMITER ;