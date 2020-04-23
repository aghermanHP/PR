<template>
  <v-card
    max-width="auto"
    class="mx-auto"
  >
   <template v-for="(item) in items">
        <v-list-item
          :key="item.from"
        >
          <v-list-item-content>
            <v-list-item-title v-html="item.from"></v-list-item-title>
            <v-list-item-subtitle v-html="item.subject"></v-list-item-subtitle>
            <v-list-item-subtitle v-html="item.content"></v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </template>
  </v-card>
</template>

<script>
  export default {
    data: () => ({
      apiLink: "http://localhost:5000/mail",
      items: null
    }),
  
  mounted(){
    this.getMails()
  },
  methods:{
    getMails(){
    this.axios.request(this.apiLink, {
      method: 'GET',
      params: {
      password:'Ghera123Ad', 
      email:'tsetsmtp@gmail.com'
      }
    }).then((response) => {
      this.items = response.data.mails
  console.log(response.data.status)
}).catch((error) => {
  console.log(error)
})
    }
  }
  }
</script>