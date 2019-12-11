<template>
    <div class="login-screen">
        <h1>Login</h1>
        <form class="login-wrapper">
            <label>Email (Ivy Tech Only):</label>
            <input type="email" name="email" />
            <label>Password:</label>
            <input type="password" name="password" />
            <input type="submit" value="Submit" />
            <a href="">New Gladiator? (Create Account)</a>
        </form>
    </div>
</template>

<script>

export default {
    name: 'LoginScreen',
    components: {}
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
form.login-wrapper input[type="email"], form.login-wrapper input[type="password"] {
    width: 100%;
    margin: 10px 0;
    height: 30px;
    border: none;
    outline: none;
    background-color: #F3D8BE;
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
    background-color: #35ECB9;
    border-radius: 5px;
    align-self: flex-end;
}
form.login-wrapper a {
    color: #0e0e0e;
    text-decoration: none;
    align-self: center;
    margin-top: 30px;
    font-weight: bold;
}
</style>