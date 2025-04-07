DELIMITER $$

CREATE TRIGGER prevenir_eliminacion_usuario
BEFORE DELETE ON usuarios
FOR EACH ROW
BEGIN
    DECLARE transacciones_count INT;
    
    SELECT COUNT(*) INTO transacciones_count FROM transacciones WHERE usuario_responsable = OLD.id_usuario;
    
    IF transacciones_count > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No se puede eliminar un usuario con transacciones registradas.';
    END IF;
END $$

DELIMITER ;