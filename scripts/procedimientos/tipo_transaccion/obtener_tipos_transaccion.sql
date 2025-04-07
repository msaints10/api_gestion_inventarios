DELIMITER $$

CREATE PROCEDURE obtener_tipos_transaccion()
BEGIN
    SELECT * FROM tipos_transaccion;
END $$

DELIMITER ;
