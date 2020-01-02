<template>
    <div class="app-screen">
        <h1>Gladiator Recruitment</h1>
        <form v-on:submit="submit" class="login-wrapper">
            <label>First Name:</label>
            <input v-model="fName" type="text" name="fname" />
            <label>Last Name:</label>
            <input v-model="lName" type="text" name="lname" />
            <label>Email (Ivy Tech Only):</label>
            <input v-model="email" type="email" name="email" />
            <label>Password:</label>
            <input v-model="password" type="password" name="password" />
            <label>Confirm Password:</label>
            <input v-model="passwordConf" type="password" name="password-conf" />
            <input type="submit" value="Submit" />
            <router-link to="/">Already have an account? (Login)</router-link>
        </form>
    </div>
</template>

<script>
import sha256 from 'crypto-js/sha256'
import Base64 from 'crypto-js/enc-base64'
import { log, error, URL } from '../globals'
import '../assets/css/formPages.css'

export default {
    name: 'SignupScreen',
    components: {},
    data: () => ({
        fName: '',
        lName: '',
        email: '',
        password: '',
        passwordConf: '',
    }),
    methods: {
        submit(e) {
            e.preventDefault()
            const { fName, lName, email, password, passwordConf } = this;
            if (
                fName.length > 0 && lName.length > 0 &&
                password.length >= 10 && password === passwordConf &&
                email.includes('@ivytech.edu')
            ) {
                log(`Signing up with: ${this.fName}, ${this.lName} ${this.email}, ${this.password}`)
                fetch(`${URL}/auth/register`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        'First_Name': this.fName,
                        'Last_Name': this.lName,
                        'Email': this.email,
                        'Password': Base64.stringify(sha256(this.password))
                    })
                })
                    .then(res => res.json())
                    .then(res => {
                        if (res.success) {
                            log('Success!!!!')
                            log(res)
                        } else if (res.error) {
                            log('\n\nSomething went wrong...')
                            error(res.error)
                        } else {
                            log(res)
                        }
                    })
                    .catch(err => error(err))
            } else {
                log('Invalid information');
            }
        },
    },
}
</script>

<style scoped>
</style>