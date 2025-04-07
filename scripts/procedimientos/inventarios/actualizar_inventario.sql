DELIMITER $$

CREATE PROCEDURE actualizar_inventario(
    IN p_id_inventario INT,
    IN p_id_producto INT,
    IN p_id_almacen INT,
    IN p_cantidad INT
)
BEGIN
    UPDATE inventario
    SET id_producto = p_id_producto,
        id_almacen = p_id_almacen,
        cantidad = p_cantidad,
        fecha_actualizacion = SYSDATE()
    WHERE id_inventario = p_id_inventario;
END $$

DELIMITER ;
