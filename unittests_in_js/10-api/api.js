const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const PORT = 7865;

app.use(bodyParser.json());

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

app.get('/available_payments', (req, res) => {
    res.json({
        payment_methods: {
            credit_cards: true,
            paypal: false
        }
    });
});

app.post('/login', (req, res) => {
    const { userName } = req.body;
    res.send(`Welcome ${userName}`);
});

module.exports = app;
