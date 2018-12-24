<template>
<div class="limiter">
    <div class="container-login100">
        <div class="wrap-login100" style="width: 75%">
            <form class="wrap-input100" v-on:submit="createANewRegUser">

              <span class="login100-form-title">
						  Create an Account
					    </span>

              <div class="wrap-input100 validate-input" data-validate = "Image is a required field">
                  Upload a profile picture (Link of the photo): 
                  <input  type="url" name="Photo" placeholder="" v-model="RegUser_photo">
              <span class="focus-input100"></span>
              </div>

              <div class="wrap-input100 validate-input"  data-validate = "Name is a required field">
                  Name:
                  <input class="input100" type="text" name="Name" placeholder=""  v-model="RegUser_name">
                  <span class="focus-input100"></span>
              </div>

              <div class="wrap-input100 validate-input" data-validate = "Surname is a required field">
                  Surname:
                  <input class="input100" type="text" name="Surname" placeholder=""  v-model="RegUser_surname">
                  <span class="focus-input100"></span>
              </div>  

              <div class="wrap-input100 validate-input" data-validate = "Birthday is a required field">
                  Birthday: 
                  <input class="input100" type="date" name="Birthday" placeholder=""  v-model="RegUser_birthday">
                  <span class="focus-input100"></span>
              </div>

              <div class="wrap-input100 validate-input" data-validate = "Valid email is required: ex@abc.xyz">
                  Email:
                  <input class="input100" type="text" name="email" placeholder=""  v-model="RegUser_email">
                  <span class="focus-input100"></span>
              </div>

              <div class="wrap-input100 validate-input" data-validate = "Address is a required field">
                  Street Address:
                  <input class="input100" type="text" name="Address" placeholder=""  v-model="RegUser_streetaddress">
                  <span class="focus-input100"></span>
              </div>

              <div class="wrap-input100 validate-input" data-validate = "Valid city is required">
                  City:
                  <input class="input100" type="text" name="city" placeholder=""  v-model="RegUser_city">
                  <span class="focus-input100"></span>
              </div>

              <div class="wrap-input100 validate-input" data-validate = "Valid contry is required">
                  Contry:
                  <input class="input100" type="text" name="contry" placeholder=""  v-model="RegUser_contry">
                  <span class="focus-input100"></span>
              </div>

              <div class="wrap-input100 validate-input" data-validate = "Valid contry is required">
                  Zip Code:
                  <input class="input100" type="text" name="contry" placeholder=""  v-model="RegUser_zipcode">
                  <span class="focus-input100"></span>
              </div>

              <div class="wrap-input100 validate-input" data-validate = "Username is required">
                  Username:
                  <input class="input100" type="text" name="Username" placeholder=""  v-model="RegUser_username">
                  <span class="focus-input100"></span>
              </div>

              <div class="wrap-input100 validate-input" data-validate = "Password is a required field">
                  Password:
                  <input class="input100" type="password" crypt="bcrypt" work="cost:11" salt="username" name="Password" placeholder=""  v-model="RegUser_password">
                  <span class="focus-input100"></span>
              </div>

                <div class="container-login100-form-btn">
                    <button class="login100-form-btn">
                       Create user
                    </button>
                </div>
                
            </form>
        </div>
    </div>
</div>
</template>
<script>
import axios from 'axios'

export default {

  data () {
    return {
    RegUser_name: '',
    RegUser_surname: '',
    RegUser_email: '',
    RegUser_username: '',
    RegUser_birthday: '',
    RegUser_photo: '',
    RegUser_password: '',
    RegUser_city: '',
    RegUser_contry: '',
    RegUser_zipcode: '',
    RegUser_streetaddress: ''



    }
  },

  methods: {

    createANewRegUser() {
    axios.post('http://127.0.0.1:8000/api/regUsers/', {
    RegUser_name: this.RegUser_name,
    RegUser_surname: this.RegUser_surname,
    RegUser_email: this.RegUser_email,
    RegUser_username: this.RegUser_username,
    RegUser_birthday: this.RegUser_birthday,
    RegUser_photo: this.RegUser_photo,
    RegUser_password: this.RegUser_password,
    RegUser_contry: this.RegUser_contry,
    RegUser_city: this.RegUser_city,
    RegUser_zipcode: this.RegUser_zipcode,
    RegUser_streetaddress: this.RegUser_streetaddress
  })
  .then(function (response) {
    alert('The User was created succesfully!!!!');
    console.log(response);
  })
  .catch(function (error) {
    alert('The User was not created, please check your data in the input fields and then try again!!!!');
    console.log(error);
  }),
  axios.post('http://127.0.0.1:8000/api/users/', {
    username: this.RegUser_username,
    password: this.RegUser_password,
    email: this.RegUser_email
  })
  .then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    console.log(error);
  })
    }
  }
}
</script>

<style scoped>
    @import "./assets/main.css";
</style>
