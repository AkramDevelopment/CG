<template>
  <div class="home-wrapper">
    <NavBar />
    <div class="app-screen">
      <h1 v-if="isAdmin">Admin Dashboard</h1>
      <h1 v-else>Welcome To The Arena</h1>

      <button class="logout" v-on:click="logout">Logout</button>
      <div v-for="p in posts" v-bind:key="`${p.type}${p.id}`" class="post-wrapper">
        <b-card class="post announcement" v-if="p.type === postTypes.announcement" v-bind:title="p.title">
          <b-card-text>
            {{ p.body }}
          </b-card-text>
        </b-card>
        <b-card class="post event" v-if="p.type === postTypes.event" v-bind:title="p.event_title">
          <div class="event-row">
            <p>{{ p.date_start !== p.date_end ? `From ${p.date_start} to ${p.date_end}` : `On ${p.date_start}` }}</p>
            <p>{{ `Starts at ${p.time_start}, Ends at ${p.time_end}` }}</p>
          </div>
          <p>{{ `Location: ${p.location}` }}</p>
        </b-card>
      </div>
      <h4 v-if="posts.length <= 0">
        Looks like we don't have any posts yet.<br />
        Please check back later!
      </h4>
    </div>
  </div>
</template>

<script>
<<<<<<< HEAD
import { log, URL, postTypes } from '../globals'
import NavBar from './NavBar.vue';
import { GET, checkAdmin } from '../helpers'

export default {
    name: 'HomeScreen',
    components: {NavBar},
    data: () => ({
        postTypes,
        announcements: [],
        events: [],
        posts: [],
        isAdmin: false
    }),
    created() {
        this.getAnnouncements()
        this.getEvents()
        checkAdmin((bool)=> {
            this.isAdmin = bool
        })
    },
    methods: {
     
        sortPosts() {
            const allPosts = []
            this.announcements.forEach(a => {
                allPosts.push({ ...a, type: postTypes.announcement })
                log(a)
            })
            this.events.forEach(e => {
                allPosts.push({ ...e, type: postTypes.event })
                log(e)
            })
            // Sort by: announcements -> Create_Date; events -> date_start
            allPosts.sort((a, b) => {
                const date1 = a.type === postTypes.announcement ? a['Create_Date'] : a['date_start']
                const date2 = b.type === postTypes.announcement ? b['Create_Date'] : b['date_start']
                return date1 - date2 // double check that the two different date types are comparable
            })
            this.posts = allPosts
        },
        getAnnouncements() {
            GET(`${URL}/announcements/view/all`)
                .then(res => {
                    if (res.ok) {
                        this.announcements = res.announcements
                        this.sortPosts()
                    } else if (res.status == 401) {
                        this.$router.push('/')
                    } else {
                        log(res)
                    }
                })
        },
        getEvents() {
            GET(`${URL}/events/all`)
                .then(res => {
                    if (res.ok) {
                        this.events = res.events
                        this.sortPosts()
                    } else if (res.status == 401) {
                        this.$router.push('/')
                    } else {
                        log(res)
                    }
                })
        },
        logout() {
            GET(`${URL}/auth/logout`)
                .then(res => {
                    if (res.ok) {
                        this.$router.push('/')
                    } else {
                        log(res)
                    }
                })
=======
import { log, URL, postTypes } from "../globals";
import NavBar from "./NavBar.vue";
import { GET } from "../helpers";

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
    this.checkAdmin();
  },
  methods: {
    checkAdmin() {
      GET(`${URL}/user/isadmin`).then(res => {
        if (res.ok) {
          this.isAdmin = true;
        } else if (res.status == 401) {
          this.isAdmin = false;
        } else {
          log(res);
        }
      });
    },
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
        const date1 = a.type === postTypes.announcement ? a.Create_Date : a.date_start;
        const date2 = b.type === postTypes.announcement ? b.Create_Date : b.date_start;
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
>>>>>>> Staging
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
  background-color: rgba(2,37,53,0.7);
  box-shadow: 0 2px 4px 2px rgba(0,0,0,0.5);
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
div.event-row {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  /* padding: 0 40px; */
}
</style>
