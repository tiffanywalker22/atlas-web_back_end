const express = require('express');
const router = require ('./routes');

const app = express();
const PORT = 1245;

app.use('/', router);

app.listen(PORT, () => {
    console.log(`Server is listening on port ${PORT}`);
});

module.exports = app;
