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
  <div class="text-center">
    <v-bottom-sheet v-model="sheet" persistent>
      <v-sheet class="text-center" height="100%">
        <v-row>
        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            v-model="email"
            :rules="emailRules"
            label="email from"
            required
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
            :rules="[rules.required, rules.min]"
            :type="show2 ? 'text' : 'password'"
            name="input-10-2"
            label="Visible"
            hint="At least 8 characters"
            v-model="password"
            class="input-group--focused"
            @click:append="show2 = !show2"
          ></v-text-field>
        </v-col>
        </v-row>
        <v-btn
          class="mt-6"
          flat
          color="error"
          @click="getMails(email, password)"
        >check inbox</v-btn>
      </v-sheet>
    </v-bottom-sheet>
  </div>
  </v-card>
</template>

<script>
  export default {
    data: () => ({
      apiLink: "http://localhost:5000/mail",
      items: null,
      show2: false,
      sheet: true,
      email: '',
      password: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+/.test(v) || 'E-mail must be valid',
      ],
      rules: {
          required: value => !!value || 'Required.',
          min: v => v.length >= 8 || 'Min 8 characters',
          emailMatch: () => ('The email and password you entered don\'t match'),
        },
    }),
  
  mounted(){
  },
  methods:{
    getMails(mail, pass){
    this.axios.request(this.apiLink, {
      method: 'GET',
      params: {
      password: pass, 
      email: mail
      }
    }).then((response) => {
      this.items = response.data.mails
  console.log(response.data.status)
  this.sheet = false
}).catch((error) => {
  console.log(error)
})
    }
  }
  }
</script>