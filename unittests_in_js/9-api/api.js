const express = require('express');

const app = express();
const PORT = 7865;

app.listen(PORT, () => {
    console.log(`API available on localhost port ${PORT}`);
});

app.param('id', (req, res, next, id) => {
    if (!/^\d+$/.test(id)) {
        return res.status(404).send('Not Found');
    }
    next();
});

app.get('/', (req, res) => {
    res.send('Welcome to the payment system');
});

app.get('/cart/:id', (req, res) => {
    res.send(`Payment methods for cart ${req.params.id}`);
});

module.exports = app;
