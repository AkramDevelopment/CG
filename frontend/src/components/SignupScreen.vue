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
          <label>First Name</label>
          <md-input v-model="fName" ></md-input>
        </md-field>

         <md-field>
          <label>Last Name</label>
          <md-input v-model="lName" ></md-input>
        </md-field>

        <md-field>
          <label>E-mail</label>
          <md-input v-model="email" ></md-input>
        </md-field>

         <md-field>
          <label>Password</label>
          <md-input v-model="password" type="password" ></md-input>
        </md-field>

        <md-field>
          <label>Confirm Password</label>
          <md-input v-model="passwordConf" type="password" ></md-input>
        </md-field>



          <div class="actions md-layout md-alignment-center-space-between">
        <md-button class="md-raised md-secondary" @click="submit">Submit Application </md-button>
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
  name: "SignupScreen",
  components: {},
  data: () => ({
    fName: "",
    lName: "",
    email: "",
    password: "",
    passwordConf: ""
  }),
  methods: {
    submit(e) {
      e.preventDefault();
      const { fName, lName, email, password, passwordConf } = this;
      if (
        fName.length > 0 &&
        lName.length > 0 &&
        password.length >= 10 &&
        password === passwordConf &&
        email.includes("@ivytech.edu")
      ) {
        POST(`${URL}/auth/register`, {
          "first-name": this.fName,
          "last-name": this.lName,
          email: this.email,
          password: Base64.stringify(sha256(this.password))
        }).then(res => 
        { log(res)
          if (res.ok) {
            log("Success!!!!");
            this.$router.push("/");
          } else {
            log(res);
          }
        });
      } else {
        log("Invalid information");
      }
    }
  }
};
</script>

<style scoped></style>
