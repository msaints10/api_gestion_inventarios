DELIMITER $$

CREATE PROCEDURE obtener_inventario(
    IN p_id_inventario INT
)
BEGIN
    SELECT * FROM inventario
    WHERE id_inventario = p_id_inventario;
END $$

DELIMITER ;
