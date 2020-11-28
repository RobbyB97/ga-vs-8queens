const express = require('express');
const path = require('path');
const chalk = require('chalk');

const publicPath = path.join(__dirname, '../../public/');
const appRoute = path.join(publicPath, 'index.html');
const wildcardRoute = path.join(publicPath, '404.html');

const router = new express.Router();


/* Routes */
router.get('*', (req, res) => {
    try {
        return res.sendFile(wildcardRoute);
    
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