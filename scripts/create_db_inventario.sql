-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema inventario
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema inventario
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `inventario` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `inventario` ;

-- -----------------------------------------------------
-- Table `inventario`.`almacenes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `inventario`.`almacenes` (
  `id_almacen` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NOT NULL,
  `direccion` VARCHAR(255) NULL DEFAULT NULL,
  `descripcion` TEXT NULL DEFAULT NULL,
  `fecha_creacion` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_almacen`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `inventario`.`tipos_transaccion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `inventario`.`tipos_transaccion` (
  `id_tipo_transaccion` INT NOT NULL AUTO_INCREMENT,
  `nombre_tipo` VARCHAR(100) NOT NULL,
  `afecta_stock` TINYINT(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_tipo_transaccion`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `inventario`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `inventario`.`usuarios` (
  `id_usuario` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `fecha_creacion` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_usuario`),
  UNIQUE INDEX `email` (`email` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `inventario`.`estados_transaccion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `inventario`.`estados_transaccion` (
  `id_estado_transaccion` INT NOT NULL AUTO_INCREMENT,
  `nombre_estado` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id_estado_transaccion`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `inventario`.`transacciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `inventario`.`transacciones` (
  `id_transaccion` INT NOT NULL AUTO_INCREMENT,
  `id_tipo_transaccion` INT NOT NULL,
  `usuario_responsable` INT NOT NULL,
  `id_almacen_origen` INT NULL DEFAULT NULL,
  `id_almacen_destino` INT NULL DEFAULT NULL,
  `fecha_transaccion` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `total_transaccion` DECIMAL(10,2) NULL DEFAULT NULL,
  `id_estado_transaccion` INT NOT NULL,
  `nota` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`id_transaccion`),
  INDEX `id_tipo_transaccion` (`id_tipo_transaccion` ASC) VISIBLE,
  INDEX `usuario_responsable` (`usuario_responsable` ASC) VISIBLE,
  INDEX `id_almacen_origen` (`id_almacen_origen` ASC) VISIBLE,
  INDEX `id_almacen_destino` (`id_almacen_destino` ASC) VISIBLE,
  INDEX `id_estado_transaccion` (`id_estado_transaccion` ASC) VISIBLE,
  CONSTRAINT `transacciones_ibfk_1`
    FOREIGN KEY (`id_tipo_transaccion`)
    REFERENCES `inventario`.`tipos_transaccion` (`id_tipo_transaccion`),
  CONSTRAINT `transacciones_ibfk_2`
    FOREIGN KEY (`usuario_responsable`)
    REFERENCES `inventario`.`usuarios` (`id_usuario`),
  CONSTRAINT `transacciones_ibfk_3`
    FOREIGN KEY (`id_almacen_origen`)
    REFERENCES `inventario`.`almacenes` (`id_almacen`),
  CONSTRAINT `transacciones_ibfk_4`
    FOREIGN KEY (`id_almacen_destino`)
    REFERENCES `inventario`.`almacenes` (`id_almacen`),
  CONSTRAINT `transacciones_ibfk_5`
    FOREIGN KEY (`id_estado_transaccion`)
    REFERENCES `inventario`.`estados_transaccion` (`id_estado_transaccion`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `inventario`.`productos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `inventario`.`productos` (
  `id_producto` INT NOT NULL AUTO_INCREMENT,
  `codigo` VARCHAR(50) NOT NULL,
  `nombre` VARCHAR(255) NOT NULL,
  `descripcion` TEXT NULL DEFAULT NULL,
  `precio_unitario` DECIMAL(10,2) NOT NULL,
  `stock_total` INT NULL DEFAULT '0',
  `fecha_creacion` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_modificacion` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_producto`),
  UNIQUE INDEX `codigo` (`codigo` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `inventario`.`detalle_transacciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `inventario`.`detalle_transacciones` (
  `id_detalle` INT NOT NULL AUTO_INCREMENT,
  `id_transaccion` INT NOT NULL,
  `id_producto` INT NOT NULL,
  `cantidad` INT NOT NULL,
  `precio_unitario` DECIMAL(10,2) NULL DEFAULT NULL,
  `subtotal` DECIMAL(10,2) NULL DEFAULT NULL,
  `id_almacen_origen` INT NOT NULL,
  `id_almacen_destino` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id_detalle`),
  INDEX `id_transaccion` (`id_transaccion` ASC) VISIBLE,
  INDEX `id_producto` (`id_producto` ASC) VISIBLE,
  INDEX `id_almacen_origen` (`id_almacen_origen` ASC) VISIBLE,
  INDEX `id_almacen_destino` (`id_almacen_destino` ASC) VISIBLE,
  CONSTRAINT `detalle_transacciones_ibfk_1`
    FOREIGN KEY (`id_transaccion`)
    REFERENCES `inventario`.`transacciones` (`id_transaccion`),
  CONSTRAINT `detalle_transacciones_ibfk_2`
    FOREIGN KEY (`id_producto`)
    REFERENCES `inventario`.`productos` (`id_producto`),
  CONSTRAINT `detalle_transacciones_ibfk_3`
    FOREIGN KEY (`id_almacen_origen`)
    REFERENCES `inventario`.`almacenes` (`id_almacen`),
  CONSTRAINT `detalle_transacciones_ibfk_4`
    FOREIGN KEY (`id_almacen_destino`)
    REFERENCES `inventario`.`almacenes` (`id_almacen`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `inventario`.`inventario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `inventario`.`inventario` (
  `id_inventario` INT NOT NULL AUTO_INCREMENT,
  `id_producto` INT NOT NULL,
  `id_almacen` INT NOT NULL,
  `cantidad` INT NOT NULL DEFAULT '0',
  `fecha_actualizacion` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_inventario`),
  INDEX `id_producto` (`id_producto` ASC) VISIBLE,
  INDEX `id_almacen` (`id_almacen` ASC) VISIBLE,
  CONSTRAINT `inventario_ibfk_1`
    FOREIGN KEY (`id_producto`)
    REFERENCES `inventario`.`productos` (`id_producto`),
  CONSTRAINT `inventario_ibfk_2`
    FOREIGN KEY (`id_almacen`)
    REFERENCES `inventario`.`almacenes` (`id_almacen`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `inventario`.`roles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `inventario`.`roles` (
  `id_rol` INT NOT NULL AUTO_INCREMENT,
  `nombre_rol` VARCHAR(100) NOT NULL,
  `descripcion` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`id_rol`),
  UNIQUE INDEX `nombre_rol` (`nombre_rol` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `inventario`.`usuarios_roles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `inventario`.`usuarios_roles` (
  `id_usuario` INT NOT NULL,
  `id_rol` INT NOT NULL,
  PRIMARY KEY (`id_usuario`, `id_rol`),
  INDEX `id_rol` (`id_rol` ASC) VISIBLE,
  CONSTRAINT `usuarios_roles_ibfk_1`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `inventario`.`usuarios` (`id_usuario`),
  CONSTRAINT `usuarios_roles_ibfk_2`
    FOREIGN KEY (`id_rol`)
    REFERENCES `inventario`.`roles` (`id_rol`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
