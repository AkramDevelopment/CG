<template>
    <div class="login-screen">
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
div.login-screen {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
}
div.login-screen > h1 {
    margin: 30px 0;
    text-transform: uppercase;
}
form.login-wrapper {
    width: 98%;
    max-width: 500px;
    border: 10px solid #a4a4a4;
    padding: 30px;
    box-sizing: border-box;
    border-radius: 30px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
}
form.login-wrapper label {
    font-size: 1.5rem;
    font-weight: bold;
}
form.login-wrapper input[type="text"],
form.login-wrapper input[type="email"],
form.login-wrapper input[type="password"] {
    width: 100%;
    margin: 10px 0;
    height: 30px;
    border: none;
    outline: none;
    background-color: var(--secondary-color);
    box-sizing: border-box;
    padding-left: 20px;
    font-size: 1.25rem;
}
form.login-wrapper input[type="submit"] {
    border: none;
    outline: none;
    padding: 10px 40px;
    font-size: 1.25rem;
    cursor: pointer;
    background-color: var(--primary-color);
    border-radius: 5px;
    align-self: flex-end;
    opacity: 0.8;
    color: #000;
    transition: 200ms ease;
}
form.login-wrapper input[type="submit"]:hover {
    opacity: 1;
    color: #fff;
}
form.login-wrapper a {
    color: #0e0e0e;
    text-decoration: none;
    align-self: center;
    margin-top: 30px;
    font-weight: bold;
}
</style>