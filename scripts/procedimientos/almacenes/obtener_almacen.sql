DELIMITER $$

CREATE PROCEDURE obtener_almacen(
    IN p_id_almacen INT
)
BEGIN
    SELECT * FROM almacenes
    WHERE id_almacen = p_id_almacen;
END $$

DELIMITER ;
