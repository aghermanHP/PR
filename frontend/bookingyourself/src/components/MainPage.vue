<template>
  <div class="hello">
    <img alt="Vue logo" src="../assets/logo.png">
    <HomeCarusel/>
  </div>
</template>

<script>
import HomeCarusel from './HomeCarusel'
export default {
  name: 'MainPage',
  components:{
    HomeCarusel
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
