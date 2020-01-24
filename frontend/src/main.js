import Vue from 'vue';
import VueRouter from 'vue-router';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue';
import App from './components/App.vue';
import LoginScreen from './components/LoginScreen.vue';
import SignupScreen from './components/SignupScreen.vue';
import HomeScreen from './components/HomeScreen.vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

Vue.config.productionTip = false;
Vue.use(VueRouter);
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);

const routes = [
  { path: '/', component: LoginScreen },
  { path: '/signup', component: SignupScreen },
  { path: '/home', component: HomeScreen },
];

const router = new VueRouter({ routes });

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
