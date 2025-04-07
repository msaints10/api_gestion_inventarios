DELIMITER $$

CREATE PROCEDURE obtener_estados_transaccion()
BEGIN
    SELECT * FROM estados_transaccion;
END $$

DELIMITER ;
