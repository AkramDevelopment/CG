<template>
  <div class="wrapper">
    <b-card title="Cyber Gladiators" class="cg-card">
      <h4>Signup Form</h4>
      <b-form class="cg-form" @submit="submit">
        <!-- First Name Input -->
        <b-form-group id="input-group-1" label="First Name:" label-for="input-1">
          <b-form-input
            id="input-1"
            v-model="fName"
            type="text"
            required
            placeholder="Enter your First Name"
          ></b-form-input>
        </b-form-group>
        <!-- Last Name Input -->
        <b-form-group id="input-group-2" label="Last Name:" label-for="input-2">
          <b-form-input
            id="input-2"
            v-model="lName"
            type="text"
            required
            placeholder="Enter your Last Name"
          ></b-form-input>
        </b-form-group>
        <!-- Email Address Input -->
        <b-form-group
          id="input-group-3"
          label="Email:"
          label-for="input-3"
          description="Must be an official IvyTech email address."
        >
          <b-form-input
            id="input-3"
            v-model="email"
            type="email"
            required
            placeholder="Enter email"
          ></b-form-input>
        </b-form-group>
        <!-- Password Input | First -->
        <b-form-group id="input-group-4" label="Password:" label-for="input-4">
          <b-form-input
            id="input-4"
            v-model="password"
            type="password"
            required
            placeholder="Enter Password"
          ></b-form-input>
        </b-form-group>
        <!-- Password Confirmation Input | Second -->
        <b-form-group id="input-group-5" label="Confirm Password:" label-for="input-5">
          <b-form-input
            id="input-5"
            v-model="passwordConf"
            type="password"
            required
            placeholder="Enter Password Again"
          ></b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary" class="cg-submit-button">Submit</b-button><br />
        <div class="cg-center-horiz">
          <router-link to="/" style="margin-top: 12px; color: #fff;"
            >Already have an account? (Login)</router-link
          >
        </div>
      </b-form>
    </b-card>
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
        }).then(res => {
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
