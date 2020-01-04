<template>
    <div class="app-screen">
        <h1>Login</h1>
        <form v-on:submit="submit" class="login-wrapper">
            <label>Email (Ivy Tech Only):</label>
            <input v-model="email" type="email" name="email" />
            <label>Password:</label>
            <input v-model="password" type="password" name="password" />
            <input type="submit" value="Submit" />
            <router-link to="/signup">New Gladiator? (Create Account)</router-link>
        </form>
    </div>
</template>

<script>
import sha256 from 'crypto-js/sha256'
import Base64 from 'crypto-js/enc-base64'
import { log, URL } from '../globals'
import { POST } from '../helpers'
import '../assets/css/formPages.css'

export default {
    name: 'LoginScreen',
    components: {},
    data: () => ({
        email: '',
        password: '',
    }),
    methods: {
        submit(e) {
            e.preventDefault()
            POST(`${URL}/auth/login`, {
                'Email': this.email,
                'Password': Base64.stringify(sha256(this.password))
            })
                .then(res => {
                    if (res.ok) {
                        this.$router.push('home')
                    } else {
                        log(res)
                    }
                })
        },
    },
}
</script>

<style scoped>
</style>