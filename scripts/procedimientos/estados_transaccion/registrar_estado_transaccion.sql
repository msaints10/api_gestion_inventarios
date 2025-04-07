DELIMITER $$

CREATE PROCEDURE registrar_estado_transaccion(
    IN p_nombre_estado VARCHAR(50)
)
BEGIN
    INSERT INTO estados_transaccion (nombre_estado)
    VALUES (p_nombre_estado);
END $$

DELIMITER ;