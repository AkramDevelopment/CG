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
import { log, error, URL } from '../globals'
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
            fetch(`${URL}/auth/login`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                credentials: 'include',
                body: JSON.stringify({
                    'Email': this.email,
                    'Password': Base64.stringify(sha256(this.password))
                })
            })
                .then(res => res.json())
                .then(res => {
                    if (res.success) {
                        this.$router.push('home')
                    } else if (res.error) {
                        // TODO: implement UI based error handling.
                        log('\n\nSomething went wrong...')
                        error(res.error)
                    } else {
                        log(res)
                    }
                })
                .catch(err => error(err))
        },
    },
}
</script>

<style scoped>
</style>