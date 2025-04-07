DELIMITER $$
CREATE PROCEDURE obtener_transacciones()
BEGIN
    SELECT * FROM transacciones;
END $$
DELIMITER ;