# Delivery bot


## How to Use

### 1. Clone repository

Clone git repository from TheBluePhoenix10/Mass-Lockdown-Marketplace

```bash
https://github.com/TheBluePhoenix10/Mass-Lockdown-Marketplace.git
```

### 2. create.env

Create a .env file with your settings in the root directory.

Always start with a new unused seed!

MAX_PAYMENT_TIME is the time until created paymentes aren't checked anymore in minutes (4320 = 3 days to pay, transactions after that are ignored)

If you want to send payouts, without receiving iotas via payments first, send the iotas to the first address of the seed (index 0)

if you want to do payments using IOTA change the "VALAUE" parameter from "0" to the desired value

```bash
SEED='REPLACEWITHEIGHTYONETRYTESEED'
IOTANODE='https://nodes.thetangle.org:443'
FALLBACKNODE='https://node01.iotatoken.nl'
MAX_PAYMENT_TIME=4320
PROVIDER_URL='http://localhost:5002/iotapay/api'
NAME="Delivery bot"
VALUE=0
```

### 3. Generate new seed

Create a seed and insert it to your .env file.

#### Linux
 enter this line in your terminal.
```bash
cat /dev/urandom |tr -dc A-Z9|head -c${1:-81}
```
### 4. Setup energy

- Insert your government provider url from [machineeconomy/akita-government](https://github.com/machineeconomy/akita-government)
- Insert your name (example: "Wind Energy")
- Insert an IOTA Value. (example: 2) 

### 5. Build the frontend

enter these lines in your terminal.
```bash
cd frontend
npm install
npm run build
cd ..
```

### 6. Run energy

enter this lines in your terminal.
```bash
npm start
```
