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



app.head('/head', async (req, res) => {

    const { key,value} = req.body;

    if (key == "123456") {
        res.status(200).json(value)
    }
    else {
        res.status(403).json({ message : "123"})
    }
});

app.get('/home', async (req, res) => {

    const body = req.body;
    res.status(200).json({Hello:"Worold!"});
    return;
});

app.put('/renew', async (req, res) => {

    const { id, pw} = req.body;

    if (id == "123456" && pw == "654321") {
        res.status(200).json({ message : "ok!"})
    }
    else {
        res.status(403).json({ message : "fail!"})
    }
});

app.post('/login', async (req, res) => {

    const { id, pw} = req.body;

    if (id == "123456" && pw == "654321") {
        res.status(200).json({ message : "ok!"})
    }
    else {
        res.status(403).json({ message : "fail!"})
    }
});

app.delete('/delete', async (req, res) => {

    const { id, pw} = req.body;

    if (id == "123456" && pw == "654321") {
        res.status(200).json({ message : "ok!"})
    }
    else {
        res.status(403).json({ message : "fail!"})
    }
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

httpServer.listen(100, () => {
    console.log('HTTP Server running on port 100');
});

/*
httpsServer.listen(443, () => {
    console.log('HTTPS Server running on port 443');
});
*/