<template>
     
  <div class="home-container">
    
      
  </div>
</template>

<script>
import { log, URL, postTypes } from "../globals";
import { GET, checkAdmin } from "../helpers";

export default {
  name: "HomeScreen",
  components: {  },
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

<style scoped>
h1 {
  color: #fff;
  font-family: Caesar, sans-serif;
}
div.post-wrapper {
  width: 50%;
  min-width: 300px;
}
@media screen and (max-width: 900px) {
  div.post-wrapper {
    width: 90%;
  }
}
div.post {
  background-color: rgba(2, 37, 53, 0.7);
  box-shadow: 0 2px 4px 2px rgba(0, 0, 0, 0.5);
  color: #fff;
  margin: 20px 0;
}
div.post h4 {
  font-family: Caesar, sans-serif;
}
div.post.announcement h4 {
  font-size: 2rem;
  font-weight: bold;
}
div.post.announcement p {
  color: #c4c4c4;
  margin-left: 10px;
  text-indent: 10px;
}
div.post.event h4 {
  font-size: 1.3rem;
}
div.post.event p {
  margin: 0;
}

.container {
  display: flex;
}
.container > div {
  flex: 1; /*grow*/
}

</style>
