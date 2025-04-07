-- Crear usuario con contraseña
CREATE USER 'api_user'@'localhost' IDENTIFIED BY 'N@qddR6_';

-- Otorgar permisos necesarios:
-- 1. Conexión a la base de datos
-- 2. Uso de procedimientos y funciones
GRANT USAGE ON *.* TO 'api_user'@'localhost';

-- Otorgar permisos a la base de datos específica (solo para ejecución de SP y funciones)
GRANT EXECUTE ON inventario.* TO 'api_user'@'localhost';

-- Asegurarse de que no tiene permisos extra como SELECT, INSERT, etc.
REVOKE ALL PRIVILEGES ON *.* FROM 'api_user'@'localhost';

-- Aplicar cambios
FLUSH PRIVILEGES;
