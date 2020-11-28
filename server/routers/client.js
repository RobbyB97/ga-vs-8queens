const express = require('express');
const path = require('path');
const chalk = require('chalk');

const publicPath = path.join(__dirname, '../../public/');
const appRoute = path.join(publicPath, 'index.html');
const wildcardRoute = path.join(publicPath, '404.html');

const router = new express.Router();


/* Routes */
router.get('/', (req, res) => {
    try {
        return res.sendFile(appRoute);
    
    } catch(e) {
        res.send(500);
        console.log(
            chalk.red('An error occured: '),
            '\n',
            `${e}`
        );
    }
});

router.get('/about', (req, res) => {
    /** Explains the project/ project abstract */

    try {
        return res.sendFile(appRoute);
    
    } catch(e) {
        res.send(500);
        console.log(
            chalk.red('An error occured: '),
            '\n',
            `${e}`
        );
    }
});

router.get('/watch', (req, res) => {
    /** Watch solutions get generated and get realtime statistics */

    try {
        return res.sendFile(appRoute);
    
    } catch(e) {
        res.send(500);
        console.log(
            chalk.red('An error occured: '),
            '\n',
            `${e}`
        );
    }
});

router.get('/docs', (req, res) => {
    /** Project documentation */

    try {
        return res.sendFile(appRoute);

    } catch(e) {
        res.send(500);
        console.log(
            chalk.red('An error occured: '),
            '\n',
            `${e}`
        );
    }
});

router.get('/contact', (req, res) => {
    /** Send the original developer an email */

    try {
        return res.sendFile(appRoute);
    
    } catch(e) {
        res.send(500);
        console.log(
            chalk.red('An error occured: '),
            '\n',
            `${e}`
        );
    }
});

router.get('/login', (req, res) => {
    /** Login for admin accounts to control Python algorithms remotely */

    try {
        return res.sendFile(appRoute);
    
    } catch(e) {
        res.send(500);
        console.log(
            chalk.red('An error occured: '),
            '\n',
            `${e}`
        );
    }
});

router.get('/register', (req, res) => {
    /** Register for admin accounts to control Python algorithms remotely */

    try {
        return res.sendFile(appRoute);
    
    } catch(e) {
        res.send(500);
        console.log(
            chalk.red('An error occured: '),
            '\n',
            `${e}`
        );
    }
});


module.exports = router;