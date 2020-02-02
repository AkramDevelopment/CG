<template>
<md-drawer :md-active.sync="showNavigation" md-swipeable>
      <md-toolbar class="md-transparent" md-elevation="0">
        <span class="md-title">Cyber<br> Gladiators</span>
      </md-toolbar>
      <hr> 
   <md-list>
     <md-list-item>
        <span class="md-list-item-text">Home</span>
        </md-list-item>

        <md-list-item>
        <span class="md-list-item-text">Meeting Notes</span>
        </md-list-item>

          <md-list-item>
        <span class="md-list-item-text">Admin</span>
        </md-list-item>

            <md-list-item>
        <span class="md-list-item-text">Roster</span>
        </md-list-item>



     </md-list> 

     





    </md-drawer>
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
  .page-container {
    min-height: 300px;
    overflow: hidden;
    position: relative;
    border: 1px solid rgba(#000, .12);
  }

  .md-drawer {
    width: 230px;
    max-width: calc(100vw - 125px);
    background-color: rgba(1, 57, 87,0.5) !important; 
  }

  .md-content {
    padding: 16px;
  }

  .md-title{ 
    font-size: 1.rem !important;
    padding-top: 30px !important; 
  }
  hr{ 
    margin-top:10px !important;
    margin-bottom: 8px !important
  }
.md-list{
background: none !important;
}

.md-list-item{
border-bottom: 1px solid rgba(255,255,255,0.5) !important;
}


.md-list-item:hover{
background-color: rgba(255,255,255,0.1)
}
</style>