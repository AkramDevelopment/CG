<template>
    <footer class="app-footer" :style="{ backgroundImage: `url('${background}')` }">
        <div class="overlay">
            <div class="angle" />
        </div>
    </footer>
</template>

<script>
import background from '../assets/img/CGBackground.jpg'
export default {
    name: 'Footer',
    data() { return { background } }
}
</script>

<style scoped>
footer.app-footer {
    width: 100%;
    height: calc(100vh - 0px);
    position:fixed;
    left: 0;
    bottom: 0;
    margin: 0;
    /* display: flex;
    align-items: center;
    justify-content: center; */
    overflow: hidden;
    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
    filter: grayscale(30%);
}
footer.app-footer > div.overlay > div.angle {
    width: 200%;
    height: 400%;
    transform: rotateZ(50deg);
    position: absolute;
    top: 20%;
    opacity: 0.5;
}
footer.app-footer h1 {
    font-size: 2.5rem;
    text-transform: uppercase;
}
</style>