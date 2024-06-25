const express = require('express');
const redis = require('redis');
const { promisify } = require('util');


const listProducts = [
    { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
    { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
    { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
    { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];


function getItemById(id) {
    return listProducts.find(item => item.id === id);
}


const app = express();
const port = 1245;


const client = redis.createClient();
client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', (err) => console.log('Redis client not connected to the server:', err));


const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);


async function reserveStockById(itemId, stock) {
    await setAsync(`item.${itemId}`, stock);
}


async function getCurrentReservedStockById(itemId) {
    const stock = await getAsync(`item.${itemId}`);
    return stock ? parseInt(stock, 10) : null;
}


app.get('/list_products', (req, res) => {
    const products = listProducts.map(product => ({
        itemId: product.id,
        itemName: product.name,
        price: product.price,
        initialAvailableQuantity: product.stock
    }));
    res.json(products);
});

app.get('/list_products/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId, 10);
    const product = getItemById(itemId);

    if (!product) {
        res.json({ status: 'Product not found' });
        return;
    }

    const currentStock = await getCurrentReservedStockById(itemId) ?? product.stock;
    res.json({
        itemId: product.id,
        itemName: product.name,
        price: product.price,
        initialAvailableQuantity: product.stock,
        currentQuantity: currentStock
    });
});

app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId, 10);
    const product = getItemById(itemId);

    if (!product) {
        res.json({ status: 'Product not found' });
        return;
    }

    const currentStock = await getCurrentReservedStockById(itemId) ?? product.stock;

    if (currentStock <= 0) {
        res.json({ status: 'Not enough stock available', itemId });
        return;
    }

    await reserveStockById(itemId, currentStock - 1);
    res.json({ status: 'Reservation confirmed', itemId });
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
