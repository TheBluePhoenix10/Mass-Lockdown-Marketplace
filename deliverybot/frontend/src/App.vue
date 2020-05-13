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
    let self = this
    setTimeout(function() {
        // click on button
        self.getInfo();
      }, 10000);
  },
  methods: {
    paymentSuccess() {
      this.payed = true;

      setTimeout(function() {
        // click on button
        location.reload();
      }, 10000);
      
    },
    getInfo() {
      this.$http.get('http://localhost:5001/info')
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
  --akita-primary: #00b0f0;
  --akita-secondary: #00fb92;
  --akita-dark: #3b3838;
  --akita-light: #f2f2f2;
  --akita-blue: #00b0f0;
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
  margin-top: 60px;

  border-radius: 10px;
  padding: 20px 20px;
  max-width: 600px;
}
.title {
  font-size: 3.5em;
  font-weight: bold;
}
.sub-title {
  font-size: 3em;
  font-weight: bold;
}

h1 {
  margin-top: 0;
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
  width: 30%;
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

.wind_gif {
  width: 100%;
}
.wind_img {
  width: 50%;
  -webkit-transform: scaleX(-1);
  transform: scaleX(-1); 
}
</style>
