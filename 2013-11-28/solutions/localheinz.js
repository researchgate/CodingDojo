var http,
    data,
    options,
    request,
    response;

/**
 * Returns a string suitable for sending to the Christmas tree server.
 *
 * @param delay
 * @returns {string}
 */
function getSpiralData(delay) {

    var frames = [

        '1111' +
        '0000' +
        '0000' +
        '0000',

        '0111' +
        '0001' +
        '0000' +
        '0000',

        '0011' +
        '0001' +
        '0001' +
        '0000',

        '0001' +
        '0001' +
        '0001' +
        '0001',

        '0000' +
        '0001' +
        '0001' +
        '0011',

        '0000' +
        '0000' +
        '0001' +
        '0111',

        '0000' +
        '0000' +
        '0000' +
        '1111',

        '0000' +
        '0000' +
        '1000' +
        '1110',

        '0000' +
        '1000' +
        '1000' +
        '1100',

        '1000' +
        '1000' +
        '1000' +
        '1000',

        '1100' +
        '1000' +
        '1000' +
        '0000',

        '1110' +
        '1000' +
        '0000' +
        '0000',
    ];

    prefix = delay + '-';

    return prefix + frames.join('\n' + prefix);
}

data = getSpiralData();

http = require('http');

options = {
    hostname: '192.168.178.134',
    port: 8080,
    method: 'POST',
    headers: {
        'Content-Type': 'text/plain',
        'Content-Length': data.length
    }
};

request = http.request(options, function(response) {
    console.log('Status: ' + response.statusCode);
    console.log('Headers: ' + JSON.stringify(response.headers));
});

request.on('error', function (error) {
    console.log('Problem: ' + error.message);
});

request.write(data);
request.end();
