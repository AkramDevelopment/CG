<template>
    <div class="app-screen">
        <h1>Dashboard</h1>
        <button class="logout" v-on:click="logout">Logout</button>
        <div v-for="a in announcements" v-bind:key="a.title" class="annoucement-card">
            <h3>Announcement Title</h3>
        </div>
        <h4 v-if="announcements.length <= 0">Looks like we don't have any announcements yet.<br /> Please check back later!</h4>
    </div>
</template>

<script>
import { log, error, reqErrors, URL } from '../globals'

export default {
    name: 'HomeScreen',
    components: {},
    data: () => ({
        announcements: []
    }),
    created() {
        this.getAnnouncements()
    },
    methods: {
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
                    } else {
                        log(res)
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
/* Announcement Card */
div.annoucement-card {
    width: 50%;
    min-width: 300px;
    padding: 20px;
    box-sizing: border-box;
    border-radius: 8px;
    border: 10px solid #a4a4a4;
    margin-bottom: 20px;
}
div.annoucement-card h3 {
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