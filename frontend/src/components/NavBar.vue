<template>
  <div class="navbar-wrapper">
    <div class="sidenav">
      <a href="#">Home</a>
      <b-dropdown class="navbar_dropdown" text=" Admin " v-if="isAdmin" href="#">
        <b-dropdown-item>Announcements</b-dropdown-item>
        <b-dropdown-item> Meeting Notes </b-dropdown-item>
        <b-dropdown-item>Create Events</b-dropdown-item>
        <b-dropdown-item>Account Applications</b-dropdown-item>
        <b-dropdown-item>Emails</b-dropdown-item>
      </b-dropdown>
      <a href="#">Meeting Minutes</a>
      <a href="#">Contact</a>
    </div>

    <!-- Page content -->
    <div class="main">
      ...
    </div>
  </div>
</template>

<script>
import { checkAdmin } from "../helpers";

export default {
  name: "NavBar",
  data: () => ({ isAdmin: false }),

  created() {
    checkAdmin(bool => {
      this.isAdmin = bool;
    });
  }
};
</script>
