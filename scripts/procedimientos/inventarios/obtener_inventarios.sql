DELIMITER $$

CREATE PROCEDURE obtener_inventarios()
BEGIN
    SELECT * FROM inventario;
END $$

DELIMITER ;
