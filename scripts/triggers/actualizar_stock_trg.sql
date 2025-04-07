CREATE TRIGGER actualizar_stock_total
AFTER INSERT ON inventario
FOR EACH ROW
UPDATE productos
SET stock_total = (
    SELECT SUM(cantidad) FROM inventario WHERE id_producto = NEW.id_producto
)
WHERE id_producto = NEW.id_producto;
