<template>
  <div class='home-wrapper' >
    <NavBar/>

      <div class="md-display-2"  > 
        Cyber Gladiators
        <div class="md-subheading">Welcome To The Arena!</div>

        </div>  

        <md-divider></md-divider>
    <div class="announcements"> </div>  
   <md-layout  >

     

   </md-layout>

  <md-divider></md-divider>
   <md-layout class ="md-layout" md-flex-xsmall="100" md-flex-small="100" md-flex-medium="100" md-flex-large="100" md-flex-xlarge="100">

   
   </md-layout>
    
  </div>

     
 

</template>

<script>
import { log, URL, postTypes } from "../globals";
import NavBar from './NavBar.vue';
import { GET, checkAdmin } from "../helpers";


export default {
  name: "HomeScreen",
  components: { NavBar },
  data: () => ({
    postTypes,
    announcements: [],
    events: [],
    posts: [],
    isAdmin: false
  }),
  created() {
    this.getAnnouncements();
    this.getEvents();
    checkAdmin(bool => {
      this.isAdmin = bool;
    });
  },
  methods: {
    sortPosts() {
      const allPosts = [];
      this.announcements.forEach(a => {
        allPosts.push({ ...a, type: postTypes.announcement });
        log(a);
      });
      this.events.forEach(e => {
        allPosts.push({ ...e, type: postTypes.event });
        log(e);
      });
      // Sort by: announcements -> Create_Date; events -> date_start
      allPosts.sort((a, b) => {
        const date1 = a.type === postTypes.announcement ? a["Create_Date"] : a["date_start"];
        const date2 = b.type === postTypes.announcement ? b["Create_Date"] : b["date_start"];
        return date1 - date2; // double check that the two different date types are comparable
      });
      this.posts = allPosts;
    },
    getAnnouncements() {
      GET(`${URL}/announcements/view/all`).then(res => {
        if (res.ok) {
          this.announcements = res.announcements;
          this.sortPosts();
        } else if (res.status == 401) {
          this.$router.push("/");
        } else {
          log(res);
        }
      });
    },
    getEvents() {
      GET(`${URL}/events/all`).then(res => {
        if (res.ok) {
          this.events = res.events;
          this.sortPosts();
        } else if (res.status == 401) {
          this.$router.push("/");
        } else {
          log(res);
        }
      });
    },
    logout() {
      GET(`${URL}/auth/logout`).then(res => {
        if (res.ok) {
          this.$router.push("/");
        } else {
          log(res);
        }
      });
    }
  }
};
</script>

<style  scoped>
  
.md-layout-item {
  height: 40px;}


.h1{
  color:white;
}


.md-layout-item {
    height: 40px;

    }
.md-layout-item::after
{
  width: 100%;
  height: 100%;
  display: block;
  background: md-get-palette-color(red, 200) !important;
  content: "";
}

.md-layout{
  
}
.md-title{

  text-align: center;
  color: black;

 
}

.md-card{
  background-color: white !important;
}

.home-header{
  text-align: center !important;
}
.md-display-2
{
  margin-top: 15px;
  text-align: center !important;
}

.announcements{

  margin-top: 20px !important;

}

</style>