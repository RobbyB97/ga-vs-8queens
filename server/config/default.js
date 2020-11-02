/* 
 * Server configuration
 */

const config = {
    http: {
        port: process.env.HTTP_PORT,
    },
    mongodb: {
        dbpath: './server/database/db',
        port: '27017',
    },
};

module.exports = config;