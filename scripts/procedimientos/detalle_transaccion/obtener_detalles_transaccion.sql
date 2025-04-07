DELIMITER $$
CREATE PROCEDURE obtener_detalles_transaccion()
BEGIN
    SELECT * FROM detalle_transacciones;
END $$
DELIMITER ;