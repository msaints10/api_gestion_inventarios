DELIMITER $$

CREATE PROCEDURE obtener_almacenes()
BEGIN
    SELECT * FROM almacenes;
END $$

DELIMITER ;
