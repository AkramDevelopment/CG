<template>
  <div id="app">
    <Header />
<<<<<<< HEAD

=======
>>>>>>> Staging
    <router-view></router-view>
  </div>
</template>

<script>
import Header from "./Header.vue";

<<<<<<< HEAD

import '../assets/css/app.css'
=======
import "../assets/css/app.css";
>>>>>>> Staging

export default {
  name: "app",
  components: {
<<<<<<< HEAD
    Header,
  
=======
    Header
>>>>>>> Staging
  }
};
</script>

<style>
:root {
  --primary-color: #66baa7;
  --secondary-color: #f3d8be;
}
* {
  margin: 0;
  padding: 0;
}
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -moz-osx-font-smoothing: grayscale;
  width: 100%;
  min-height: 100vh;
  background-color: #494b48;
}
</style>
