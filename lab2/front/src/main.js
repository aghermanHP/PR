import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import VueAxios from 'vue-axios'
import vuetify from './plugins/vuetify'
import mdi from 'vue-material-design-icons/styles.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'

 
Vue.use(VueAxios, axios)
Vue.use(mdi)
Vue.config.productionTip = false

new Vue({
  axios,
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
