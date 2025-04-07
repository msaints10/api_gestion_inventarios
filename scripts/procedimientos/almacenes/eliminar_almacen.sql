DELIMITER $$

CREATE PROCEDURE eliminar_almacen(
    IN p_id_almacen INT
)
BEGIN
    DELETE FROM almacenes
    WHERE id_almacen = p_id_almacen;
END $$

DELIMITER ;
