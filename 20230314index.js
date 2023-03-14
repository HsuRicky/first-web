const https = require('https');
const http = require('http');
const fs = require('fs');

const express = require('express');
const cors = require('cors');

const app = express();
const corsOptions = {
    origin: '*',
    methods: "GET"
};

/*
app.all('*', function (req, res, next) {
    if (req.secure) {
        return next();
    }

    res.redirect('https://' + req.hostname + req.originalUrl);
});
*/

app.use(cors(corsOptions));
app.use(express.json({ limit: '10mb' }));

app.get('*', async (req, res) => {

    const body = req.body;
    res.status(200).json(body);
    return;
});

/*
const credentials = {
    key: fs.readFileSync('./ssl/private.key'),
    cert: fs.readFileSync('./ssl/certificate.crt'),
    ca: fs.readFileSync('./ssl/ca_bundle.crt'),
    requestCert: false,
    rejectUnauthorized: false
};
*/

const httpServer = http.createServer(app);
//const httpsServer = https.createServer(credentials, app);

httpServer.listen(160, () => {
    console.log('HTTP Server running on port 80');
});

/*
httpsServer.listen(443, () => {
    console.log('HTTPS Server running on port 443');
});
*/