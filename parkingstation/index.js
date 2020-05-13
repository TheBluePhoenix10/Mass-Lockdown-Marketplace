var paymentModule = require('iota-payment')
var express = require('express')
var app = express()
var cors = require('cors')
const fs = require('fs');
const dotenv = require('dotenv');
dotenv.config();

app.use(cors())

app.use('/', express.static('frontend/dist'));

app.get("/info", (req, res) => {
    paymentModule.getBalance()
        .then(balance => {
            console.log(balance)
            res.send({
                name: process.env.NAME,
                message: 'hello world!', 
                balance: balance
            });
        })
        .catch(err => {
        console.log(err)
        })
});

var options = {
    websockets: true,
    api: true
    // ...
}

let server = paymentModule.createServer(app, options)


//Create an event handler which is called, when a payment was successfull
var onPaymentSuccess = function (payment) {
    console.log('onPaymentSuccess::', payment)
    var child = require('child_process').exec('python parking.py')
    child.stdout.pipe(process.stdout)
    child.on('exit', function() {
    })
}
paymentModule.on('paymentSuccess', onPaymentSuccess);
paymentModule.on('payoutSent', onPaymentSuccess);

// Start server with iota-payment module on '/custom'
server.listen(5002, function () {
    console.log(`Server started on http://localhost:5002 `)
})

