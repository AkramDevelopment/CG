<template>
  <div id="app">
    <Header />
    <router-view></router-view>
  </div>
</template>

<script>
import Header from './Header.vue'
import '../assets/css/app.css'

export default {
  name: 'app',
  components: {
    Header
  }
}
</script>

<style>
:root {
  --primary-color: #66baa7;
  --secondary-color: #F3D8BE;
}
* { margin: 0; padding: 0; }
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 100%;
  min-height: 100vh;
  background-color: #1e1e1e;
}
</style>
