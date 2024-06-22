const express = require('express');

const app = express();

app.param('id', (req, res, next, id) => {
    if (!/^\d+$/.test(id)) {
        return res.status(404).send('Not Found');
    }
    next();
});

const server = app.listen(process.env.PORT || 7865, () => {
    console.log(`API available on localhost port ${server.address().port}`);
});

app.get('/', (req, res) => {
    res.send('Welcome to the payment system');
});

app.get('/cart/:id', (req, res) => {
    res.send(`Payment methods for cart ${req.params.id}`);
});

module.exports = { app, server };
