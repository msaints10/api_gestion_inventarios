DELIMITER $$
CREATE PROCEDURE registrar_usuario(
    IN p_nombre VARCHAR(255),
    IN p_email VARCHAR(255),
    IN p_password VARCHAR(255)
)
BEGIN
    INSERT INTO usuarios (nombre, email, password, fecha_creacion, activo)
    VALUES (p_nombre, p_email, p_password, SYSDATE(), 1);
END $$
DELIMITER ;