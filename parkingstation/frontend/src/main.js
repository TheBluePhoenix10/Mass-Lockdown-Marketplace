import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'

Vue.config.productionTip = false
Vue.prototype.$http = axios


import VueSocketIOExt from 'vue-socket.io-extended';
import io from 'socket.io-client';

const socket = io('http://localhost:5002', { path: '/iotapay/socket' });

Vue.use(VueSocketIOExt, socket);

import { store } from './store'
import IotaPayment from 'vue-iota-payment'
Vue.use(IotaPayment, { store, url: 'http://localhost:5002', path: '/iotapay', api_path: '/iotapay/api' })


new Vue({
  store,
  render: h => h(App),
}).$mount('#app')
