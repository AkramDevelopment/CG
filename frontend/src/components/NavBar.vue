<template>

 <md-tabs md-sync-route :md-elevation:md-alignment="fixed"> 
      <md-tab id="tab-home" md-label="Home" to="/home" exact>
      </md-tab>

      <md-tab id="meeting-notes" md-label="Meeting Notes" to="/ree" exact>
      </md-tab>


      <md-tab id="suggestions" md-label="Suggestions" to="/ree" exact>
      </md-tab>

      <md-tab id="admin" md-label="Admin" to="/ree" exact>
      </md-tab>

    
    </md-tabs>
    
</template>

<script>
import { checkAdmin } from "../helpers";

export default {
  name: "NavBar",
  data: () => ({ isAdmin: false, showNavigation : true }),

  created() {
    checkAdmin(bool => {
      this.isAdmin = bool;
    });
  }
};
</script>


<style scoped> 

md-button-content{
  border-right: 1px solid white !important;
}

</style>