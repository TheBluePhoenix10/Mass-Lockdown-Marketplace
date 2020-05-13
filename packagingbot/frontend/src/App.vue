<template>
  <div id="app">
    <div class="left">
      <h3>Machine Type</h3>
      <h1 class="title">{{name}}</h1>
      <h3>Wallet Balance</h3>
      <h1 class="title">{{balance}}</h1>
      <h3>Action</h3>
      <h1 class="title">{{action}}</h1>
    </div>
    <div class="right">
      <div v-if="!payed" @click="order_product">
        <iota-payment class="pay-button" @paymentSuccess="paymentSuccess">Order Product</iota-payment>
      </div>
      <div v-else>
          <img class="robot" src="./assets/Robot002.gif" />
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'app',
  components: {
    
  },
  data() {
    return {
      payed: false,
      name: 'Loading',
      balance: 'Loading',
      action: 'Loading',
      last_tx: 'Loading'
    }
  },
  created() {
    this.getInfo()
  },
  methods: {
    paymentSuccess(payment) {
      this.payed = true;
      console.log(payment)
      setTimeout(function() {
        // click on button
        location.reload();
      }, 10000);
      
    },
    getInfo() {
      this.$http.get('http://localhost:5000/info')
      .then((result) => {
        console.log("result", result)
        this.name = result.data.name
        this.balance = result.data.balance
        this.action = 'Waiting for Work'
        this.last_tx = 'None'
      })
    },
    order_product() {
        console.log("logogogo")
       this.action = 'Waiting for Pay'
    }
  }
}
</script>

<style >
:root {
  --akita-primary: #00b1f0;
  --akita-secondary: #00fb92;
  --akita-dark: #3b3868;
  --akita-light: #f2f2f2;
  --akita-blue: #01b1f0;
}
body {
  height: 100vh;
  background: linear-gradient(
    to bottom right,
    var(--akita-primary) 50%,
    var(--akita-secondary) 85%
  );
}
#app {
  font-family: "Oswald", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: var(--akita-light);
  margin: 0 auto;

  border-radius: 10px;
  width: 100%;
}
.title {
  font-size: 3.5em;
  font-weight: bold;
  margin-top: 0
}
.sub-title {
  font-size: 3em;
  font-weight: bold;
}

h3 {
    margin-bottom: 0
}
.logo {
  width: 200px;
}

.left {
  margin-left: 50px;
  float: left;
  margin-top: 50px;
}
.right {
  margin-top: 100px;
  text-align: center;
  width: 50%;
  float: right;
}

.pay-button button {
  background-color: var(--akita-dark);
  border-radius: 10px;
  border: none;
  color: white;
  padding: 30px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 18px;
}
.pay-button a {
    display: none;
  }
.pay-button button:hover {
  cursor: pointer;
}

.robot {
  width: 50%;
}
</style>
