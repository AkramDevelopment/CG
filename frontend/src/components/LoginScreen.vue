<template>
  <div class="wrapper">
    <b-card title="Cyber Gladiators" class="cg-card">
      <h4>Login Form</h4>
      <b-form class="cg-form" @submit="submit">
        <!-- Email Address Input -->
        <b-form-group
          id="input-group-1"
          label="Email:"
          label-for="input-1"
          description="Must be an official IvyTech email address."
        >
          <b-form-input
            id="input-1"
            v-model="email"
            type="email"
            required
            placeholder="Enter email"
          ></b-form-input>
        </b-form-group>
        <!-- Password Input -->
        <b-form-group id="input-group-2" label="Password:" label-for="input-2">
          <b-form-input
            id="input-2"
            v-model="password"
            type="password"
            required
            placeholder="Enter Password"
          ></b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary" class="cg-submit-button">Submit</b-button><br />
        <div class="cg-center-horiz">
          <router-link to="/signup" class="router-link"
            >New Gladiator? (Create Account)</router-link
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

<style scoped></style>
