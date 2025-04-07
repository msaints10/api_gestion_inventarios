DELIMITER $$
CREATE PROCEDURE obtener_transaccion(
    IN p_id_transaccion INT
)
BEGIN
    SELECT * FROM transacciones WHERE id_transaccion = p_id_transaccion;
END $$
DELIMITER ;