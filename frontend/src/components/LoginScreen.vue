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
        <a href="/signup"> Register</a>
        <md-button class="md-raised md-secondary" @click="auth">Log in </md-button>
      </div>
      </div>

    

      <div class="loading-overlay" v-if="loading">
        <md-progress-spinner md-mode="indeterminate" :md-stroke="2"></md-progress-spinner>
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
 .md-content {
    z-index: 1;
    padding: 40px;
    width: 100%;
    max-width: 400px;
    position: relative;
    box-sizing: content-box;
    padding-bottom: 1px;
    background-color: rgba(0, 12, 14, 0.7) !important;
    width: 500px;
    margin: 0 !important;
    border: none !important;
    margin-bottom: 0 !important;
    border-radius: 0 !important;
    padding-bottom: 0 !important;
    height: 100%;
    font-family: Caesar !important;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

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
  .loading-overlay {

    z-index: 10;
    top: 0;
    left: 0;
    right: 0;
    position: absolute;
    width: 100%;
    height: 100%;
    background: rgba(255, 255, 255, 0.9);
    display: flex;
    align-items: center;
    justify-content: center;


  }

  .centered-container {


   display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: calc(100vh - 56px);
    padding-bottom: calc(56px * 0.5);
    
    
    
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
  
</style>
