<template>
<div>
  <div class="centered-container">
  <div class="wrapper">
    
    <md-content class="md-elevation-3">

    

      <div class="form">
          <div class="title">
        <div class="md-title">Cyber Gladiators</div>
       
      </div>
        <md-field>
          <label>E-mail</label>
          <md-input v-model="email" ></md-input>
        </md-field>

        <md-field md-has-password>
          <label>Password</label>
          <md-input v-model="password" type="password"></md-input>
        </md-field>

          <div class="actions md-layout md-alignment-center-space-between">
        <router-link to="/signup">Register</router-link>
        <md-button class="md-raised md-secondary" @click="submit">Login </md-button>
      </div>
      </div>

    </md-content>
    <div class="background" />
  </div>
    
    </div> 
   </div> 
</template>

<script>
import sha256 from "crypto-js/sha256";
import Base64 from "crypto-js/enc-base64";

import { log, URL } from "../globals";
import { POST } from "../helpers";

export default {
  name: "LoginScreen",
  components: {},
  data: () => ({
    email: "",
    password: ""
  }),
  methods: {
    submit(e) {
      e.preventDefault();
      POST(`${URL}/auth/login`, {
        email: this.email,
        password: Base64.stringify(sha256(this.password))
      }).then(res => {
        if (res.ok) {
          this.$router.push("home");
        } else {
          log(res);
        }
      });
    }
  }
};
</script>

<style scoped>

  .background {

    height: 100%;
    width: 100%;
    bottom: 0;
    left: 0;
    height: 100%;
    width: 100%;
    top: 0;
    bottom: 0;
    right: 0;
    left: 0;
    z-index: 0;

  }
  

  .centered-container {


   display: flex;
    align-items: center;
    justify-content: center;
    }

  .centered-container > title{
  margin-bottom: 30px;}

  .actions > md-button {

      margin: 0;
    }
  .form {

  
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

  
  }

  .md-input{

    color:white !important;
  }
 .md-field > label{

    color:white !important;
  }

  .md-field > border{
    color: white !important;
  }
.md-title{ 
  font-size: 30px !important;
}

.md-button { 
  margin-left: 20px !important;
}



</style>
