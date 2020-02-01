<template>
 <div class="centered-container">
  <div class="wrapper">
    <md-card title="Cyber Gladiators" class="cg-card">
            <md-card-header>
        <div class="md-title">Cyber Gladiators</div>
      </md-card-header>
      <h4>Login Form</h4>
      <md-field>
          <label>E-mail</label>
          <md-input v-model="email" autofocus></md-input>
        </md-field>

        <md-field md-has-password>
          <label>Password</label>
          <md-input v-model="password" type="password"></md-input>
        </md-field>
    
    </md-card>
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
.md-input{
  border-bottom: 0.5px solid white ! important;
  border-top: 0.5px solid white ! important;
   border-right: 0.5px solid white ! important;
  
   border-radius: 3px;
   align-content: flex;
  font-family: 'Roboto Mono', monospace;

  color:white
}

.md-card-header{ 
  color:white
}
</style>
