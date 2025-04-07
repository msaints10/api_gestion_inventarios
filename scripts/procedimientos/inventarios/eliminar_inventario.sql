DELIMITER $$

CREATE PROCEDURE eliminar_inventario(
    IN p_id_inventario INT
)
BEGIN
    DELETE FROM inventario
    WHERE id_inventario = p_id_inventario;
END $$

DELIMITER ;
