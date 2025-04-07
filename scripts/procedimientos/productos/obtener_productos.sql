DELIMITER $$

CREATE PROCEDURE obtener_productos()
BEGIN
    SELECT * FROM productos;
END $$

DELIMITER ;
