DELIMITER $$

CREATE PROCEDURE obtener_producto(
    IN p_id_producto INT
)
BEGIN
    SELECT * FROM productos
    WHERE id_producto = p_id_producto;
END $$

DELIMITER ;