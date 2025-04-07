DELIMITER $$

CREATE PROCEDURE obtener_hash_usuario (
    IN p_email VARCHAR(255)
)
BEGIN
    SELECT id_usuario, password FROM usuarios WHERE email = p_email;
END $$

DELIMITER ;
