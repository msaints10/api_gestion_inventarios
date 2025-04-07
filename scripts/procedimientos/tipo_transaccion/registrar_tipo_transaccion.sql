DELIMITER $$

CREATE PROCEDURE registrar_tipo_transaccion(
    IN p_nombre_tipo VARCHAR(100),
    IN p_afecta_stock BOOLEAN
)
BEGIN
    INSERT INTO tipos_transaccion (nombre_tipo, afecta_stock)
    VALUES (p_nombre_tipo, p_afecta_stock);
END $$

DELIMITER ;
