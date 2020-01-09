<template>
    <footer class="app-footer">
        
    </footer>
</template>

<script>
export default {
    name: 'Footer',
}
</script>

<style scoped>
footer.app-footer {
    width: 100%;
    height: 80px;
    position:fixed;
    left: 0;
    bottom: 0;
    margin: 0;
    background-color: var(--primary-color);
    display: flex;
    align-items: center;
    justify-content: center;
}
footer.app-footer h1 {
    font-size: 2.5rem;
    text-transform: uppercase;
}
</style>