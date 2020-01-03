<template>
    <div class="app-screen">
        <h1>Dashboard</h1>
        <button class="logout" v-on:click="logout">Logout</button>
        <div v-for="p in posts" v-bind:key="p.title" class="post-wrapper">
            <div v-if="p.type === postTypes.announcement" class="annoucement-card">
                <h3>Announcement Title</h3>
            </div>
            <div v-else-if="p.type === postTypes.event" class="event-card">
                <h3>Event Title</h3>
            </div>
        </div>
        <h4 v-if="posts.length <= 0">Looks like we don't have any posts yet.<br /> Please check back later!</h4>
    </div>
</template>

<script>
import { log, error, reqErrors, URL, postTypes } from '../globals'

export default {
    name: 'HomeScreen',
    components: {},
    data: () => ({
        announcements: [],
        events: [],
        posts: []
    }),
    created() {
        this.getAnnouncements()
        // this.getEvents()
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
            fetch(`${URL}/announcements/view/all`, {
                method: 'GET',
                headers: {},
                credentials: 'include'
            })
                .then(res => res.json())
                .then(res => {
                    if (res.error && res.error == reqErrors.badAuth) {
                        this.$router.push('/')
                    } else if (res.announcements) {
                        this.announcements = res.announcements
                        this.sortPosts()
                    } else {
                        log(res)
                    }
                })
                .catch(err => error(err))
        },
        getEvents() {
            fetch(`${URL}/events/all`, {
                method: 'GET',
                headers: {},
                credentials: 'include'
            })
                .then(res => res.json())
                .then(res => {
                    if (res.events) {
                        this.events = res.events
                        this.sortPosts()
                    } else {
                        print(res)
                    }
                })
                .catch(err => error(err))
        },
        logout() {
            fetch(`${URL}/auth/logout`, {
                method: 'GET',
                headers: {},
                credentials: 'include'
            })
                .then(res => res.json())
                .then(res => {
                    if (res.success) {
                        this.$router.push('/')
                    } else {
                        log(res)
                    }
                })
                .catch(err => error(err))
        }
    }
}
</script>

<style scoped>
/* Announcement Card && Event Card */
div.annoucement-card,
div.event-card {
    width: 50%;
    min-width: 300px;
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
</style>