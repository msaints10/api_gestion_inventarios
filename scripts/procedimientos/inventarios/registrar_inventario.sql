DELIMITER $$

CREATE PROCEDURE registrar_inventario(
    IN p_id_producto INT,
    IN p_id_almacen INT,
    IN p_cantidad INT
)
BEGIN
    INSERT INTO inventario (id_producto, id_almacen, cantidad, fecha_actualizacion)
    VALUES (p_id_producto, p_id_almacen, p_cantidad, SYSDATE());
END $$

DELIMITER ;
