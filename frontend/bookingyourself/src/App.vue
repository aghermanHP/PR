<template>
  <div id="app">
    <HeaderBymai class="header-position"/>
    <MainPage/>
  </div>
</template>

<script>
import MainPage from './components/MainPage.vue';
import HeaderBymai from './components/header_footer/header'

export default {
  name: 'app',
  components: {
    MainPage,
    HeaderBymai
  },
  data(){
  return{
  }
  }
}
</script>

<style>
.header-position{
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 1;
  }
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
