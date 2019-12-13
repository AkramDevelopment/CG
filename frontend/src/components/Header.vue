<template>
    <header class="app-header">
        <h1>Cyber Gladiators</h1>
    </header>
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