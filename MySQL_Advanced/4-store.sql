-- task four, buy buy buy
-- sql script that creates a trigger
CREATE TRIGGER after_order_insert
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
