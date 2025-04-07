DELIMITER $$
CREATE PROCEDURE eliminar_detalle_transaccion(
    IN p_id_detalle INT
)
BEGIN
    DELETE FROM detalle_transacciones WHERE id_detalle = p_id_detalle;
END $$
DELIMITER ;