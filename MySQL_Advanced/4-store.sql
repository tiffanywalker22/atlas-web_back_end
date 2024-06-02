-- task four, buy buy buy
-- sql script that creates a trigger
CREATE TRIGGER after_order_insert
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.quantity
    WHERE name = NEW.item_nane
END;
