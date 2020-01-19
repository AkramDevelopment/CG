<template>
    <div>
        <Footer />
        <div class="cg-center-content">
            <b-card
                title="Login to your Cyber Gladiator Account"
                class="mb-2 cg-card cg-card-size"
            >
                <b-card-text>
                    <b-form @submit="submit">
                        <!-- Email Address Input -->
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
                        <!-- Password Input -->
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
                        <b-button type="submit" variant="primary" class="cg-submit-button">Submit</b-button><br />
                        <div class="cg-center-horiz">
                            <router-link to="/signup" style="margin-top: 12px;">New Gladiator? (Create Account)</router-link>
                        </div>
                    </b-form>
                </b-card-text>
            </b-card>
        </div>
    </div>
</template>

<script>
import Footer from './Footer'
import { log, URL } from '../globals'
import { POST } from '../helpers'

export default {
    name: 'LoginScreen',
    components: {
        Footer
    },
    data: () => ({
        email: '',
        password: '',
    }),
    methods: {
        submit(e) {
            e.preventDefault()
            POST(`${URL}/auth/login`, {
                'email': this.email,
                'password': this.password
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