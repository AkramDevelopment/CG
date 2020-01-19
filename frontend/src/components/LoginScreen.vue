<template>
    <div class="center-content">
        <b-card
            title="Login"
            class="mb-2 card"
        >
            <b-card-text>
                <b-form @submit="submit">
                    <b-form-group
                        id="input-group-1"
                        label="Email:"
                        label-for="input-1"
                        description="Must be an official IvyTech email address."
                    >
                        <b-form-input
                        id="input-1"
                        v-model="email"
                        type="email"
                        required
                        placeholder="Enter email"
                        ></b-form-input>
                    </b-form-group>
                    <b-form-group
                        id="input-group-2"
                        label="Password:"
                        label-for="input-2"
                    >
                        <b-form-input
                        id="input-2"
                        v-model="password"
                        type="password"
                        required
                        placeholder="Enter Password"
                        ></b-form-input>
                    </b-form-group>
                    <b-button type="submit" variant="primary" class="submit-button">Submit</b-button><br />
                    <div class="center-horiz">
                        <router-link to="/signup" style="margin-top: 12px;">New Gladiator? (Create Account)</router-link>
                    </div>
                </b-form>
            </b-card-text>
        </b-card>
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
.center-content {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: calc(100vh - 56px);
    padding-bottom: calc(56px * 0.5);
}
.card {
    width: 50%;
    min-width: 300px;
    max-width: 800px;
}
.submit-button {
    width: 50%;
    margin-left: 25%;
}
.center-horiz {
    width: 100%;
    display: flex;
    justify-content: center;
}
</style>