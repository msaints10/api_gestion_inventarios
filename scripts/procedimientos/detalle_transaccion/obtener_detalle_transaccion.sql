DELIMITER $$
CREATE PROCEDURE obtener_detalle_transaccion(
    IN p_id_detalle INT
)
BEGIN
    SELECT * FROM detalle_transacciones WHERE id_detalle = p_id_detalle;
END $$
DELIMITER ;