<template>
    <b-navbar toggleable="lg" type="dark" variant="primary">
        <b-navbar-brand href="#">Cyber Gladiators</b-navbar-brand>
        <b-navbar-nav class="ml-auto">
            <b-button right variant="primary">Sign Out</b-button>
        </b-navbar-nav>
    </b-navbar>
</template>

<script>
export default {
    name: 'Header',
}
</script>

<style scoped>
header.app-header {
    width: 100%;
    height: 80px;
    margin: 0;
    background-color: var(--primary-color);
    display: flex;
    align-items: center;
    justify-content: center;
}
header.app-header h1 {
    font-size: 2.5rem;
    text-transform: uppercase;
}
</style>