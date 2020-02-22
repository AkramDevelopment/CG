<template>
  <div class='home-wrapper' >
    <NavBar/>

      <div class="md-display-2"  > 
        Cyber Gladiators
        <div class="md-subheading">Welcome To The Arena!</div>
        </div>  
        <md-divider></md-divider>
    <div class="current-notes"> 
      <md-card> 
        <md-card-header> <div class="md-title">Latest Update</div>
        <div class="md-subhead">2/21/2020</div></md-card-header>
        <md-card-content> Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.

The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham. </md-card-content>
        </md-card> 
      </div>  


      
   <md-layout  >
   </md-layout>

 <div class="events">
   <div class="md-display-2">  Events </div> 
  

  <div v-for="e in events" v-bind:key="e.id">
    <div class="event-row">

      <div>  
      <li> <md-icon> calendar_today</md-icon> Date: {{e.date_start}}</li> </div> 

      <li> <md-icon> calendar_today</md-icon> Location: {{e.location}}</li>
      
      
      
      </div>
      
      <md-divider> </md-divider>

     </div>
    
       
       
       </div>
      
      
     
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
        const date1 = a.type === postTypes.announcement ? a["create_date"] : a["date_start"];
        const date2 = b.type === postTypes.announcement ? b["create_date"] : b["date_start"];
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
          log(this.events)
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
  color: white !important;

 
}

.events{ 
  align-items: center;
}
.md-subheade{ 
  color:white
}


.home-header{
  text-align: center !important;
  
}
.md-display-2
{
  margin-top: 15px;
  text-align: center !important;
  color: white !important;

}

.announcements{

  margin-top: 20px !important;

}
.md-divider{ 
  margin: 20px !important;
  width : 60%;
  background-color: #039693 ! important;  
}



.current-notes{ 
  width: 50% !important;
  

}

.md-card .md-subhead{ 
  color:white !important;
}

.current-notes .md-card{ 
  background: rgba(0, 0, 0, 0.6)!important;
  box-shadow: 0px 3px 14px 1px rgba(0,0,0,.2)!important;
  border: 2px solid black;
  

}

.current-notes .md-card-header{ 
  text-align: center !important;
  font-size: 2rem !important;
  
}


.current-notes .md-card-header .md-title{ 
  color:white !important;
  
}


.md-card-content{ 
  text-overflow: ellipsis !important;
  max-width: 100% !important;
  padding: 10px 50px ! important; 
  text-indent: 20px !important;
  color:#039693 !important;
  line-height: 150% !important;
  letter-spacing: 3px;
}


.events{ 
  align-content: center !important;
  position: absolute !important;
  top: 50px;
  left:0px;
  width: 300px;
  height: calc(100vh - 50px);
  background-color: rgba(0,0,0,.2);
  color:white !important;
  list-style-type: none;
  
}

.event-row{
  align-content: center !important;
  padding-top: 20px;
}

.events .md-display-2{
  padding-top: 5px;
  padding-bottom:5px;
}
</style>