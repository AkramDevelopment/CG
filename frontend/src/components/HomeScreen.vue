<template>
    <div class="app-screen">
        <h1 v-if="isAdmin">Admin Dashboard</h1>
        <h1 v-else>Dashboard</h1>
        <button class="logout" v-on:click="logout">Logout</button>
        <div v-for="p in posts" v-bind:key="p.id" class="post-wrapper">
            <b-card v-if="p.type === postTypes.announcement" class="cg-card" v-bind:title="p.title">
                <b-card-text>
                    {{p.body}}
                </b-card-text>
            </b-card>
            <b-card v-if="p.type === postTypes.event" title="Event Name">
                No content available....
            </b-card>
        </div>
        <h4 v-if="posts.length <= 0">Looks like we don't have any posts yet.<br /> Please check back later!</h4>
    </div>
</template>

<script>
import { log, URL, postTypes } from '../globals'
import { GET } from '../helpers'

export default {
    name: 'HomeScreen',
    components: {},
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
        this.checkAdmin()
    },
    methods: {
        checkAdmin() {
            GET(`${URL}/user/isadmin`)
                .then(res => {
                    if (res.ok) {
                        this.isAdmin = true;
                    } else if (res.status == 401) {
                        this.isAdmin = false;
                    } else {
                        log(res)
                    }
                })
        },
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
        }
    }
}
</script>

<style scoped>
h1 { color: #fff; }
div.post-wrapper {
    width: 50%;
    min-width: 300px;
}
@media screen and (max-width: 900px) {
    div.post-wrapper {
        width: 90%;
    }
}
/* Announcement Card && Event Card */
div.annoucement-card,
div.event-card {
    width: 100%;
    padding: 20px;
    box-sizing: border-box;
    border-radius: 8px;
    border: 10px solid #a4a4a4;
    margin-bottom: 20px;
}
div.annoucement-card h3,
div.event-card h3 {
    font-size: 1.6rem;
}

/* Logout button */
button.logout {
    position: absolute;
    top: 110px;
    right: 40px;
    background: rgba(0, 0, 0, 0);
    outline: none;
    border: none;
    font-size: 1.5rem;
    color: var(--primary-color);
    box-sizing: border-box;
    padding: 5px 20px;
    cursor: pointer;
    border-radius: 5px;
    transition: 200ms ease;
}
button.logout:hover {
    background: rgba(0, 0, 0, 0.2);
}
h4 { color: #e0e0e0; }
</style>