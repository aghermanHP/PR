<template>
  <v-form v-model="valid">
    <v-container>
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

        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            v-model="emailDestinatary"
            :rules="emailRules"
            label="destinatary Mail"
            required
          ></v-text-field>
        </v-col>
      </v-row>

      <v-row>
          <v-col cols="12" md="6">
            <v-text-field
              v-model="subject"
              :rules="textRules"
              label="Subject"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="6">
            <v-text-field
              v-model="content"
              :rules="textRules"
              label="Text"
              required
            ></v-text-field>
          </v-col>
      </v-row>
      <v-btn @click="sendMail()">Send mail</v-btn>
    </v-container>
  </v-form>
</template>

<script>
  export default {
    data: () => ({
      valid: false,
      apiLink: "http://localhost:5000/mail",
      email: '',
      password:'xxxx',
      emailDestinatary: '',
      subject: '',
      content: '',
      show2: false,
      lastname: '',
      textRules: [
        v => !!v || 'Name is required',
        v => v.length >= 10 || 'Name must be more than 10 characters',
      ],
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

    methods:{
    sendMail(){
    this.axios.post(this.apiLink, {
      password: this.password, 
      email: this.email,
      subject: this.subject,
      message: this.content,
      receiver: this.emailDestinatary
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