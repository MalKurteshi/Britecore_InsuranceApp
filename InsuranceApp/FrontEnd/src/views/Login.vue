<template>
    <div class="limiter">
        <div class="container-login100">
            <div class="wrap-login100">

                <div class="login100-pic js-tilt" data-tilt>
                    <img src="./assets/img-01.png" alt="IMG">
                </div>

                <form class="login100-form validate-form">

					<span class="login100-form-title">
						Member Login
					</span>

                    <div class="wrap-input100 validate-input" data-validate = "Valid email is required: ex@abc.xyz">
                        <input class="input100" type="text" name="username" v-model="username" placeholder="Username" />
                        <span class="focus-input100"></span>
                        <span class="symbol-input100">
							<i class="fa fa-envelope" aria-hidden="true"></i>
						</span>
                    </div>

                    <div class="wrap-input100 validate-input" data-validate = "Password is required">
                        <input class="input100" type="password" name="password" v-model="password" placeholder="Password" />
                        <span class="focus-input100"></span>
                        <span class="symbol-input100">
							<i class="fa fa-lock" aria-hidden="true"></i>
						</span>
                    </div>

                    <div class="container-login100-form-btn">
                        <button  @click.prevent="authenticate" class="login100-form-btn" >
                            Login
                        </button>
                    </div>

                    <div class="text-center p-t-136">
                        <a href="#" class="txt2" > <router-link to="/register">
                            Create your Account</router-link>
                        </a>
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
      username: '',
      password: ''
    }
  },
  methods: {
    authenticate () {
        this.$session.start()
        this.$session.set('username', this.username)
        
      const payload = {
        username: this.username,
        password: this.password
      }

      axios.post(this.$store.state.endpoints.obtainJWT, payload)
        .then((response) => {
          this.$store.commit('updateToken', response.data.token)
          // get and set auth user
          const base = {
            baseURL: this.$store.state.endpoints.baseUrl,
            headers: {
            // Set your Authorization to 'JWT', not Bearer!!!
              Authorization: `JWT ${this.$store.state.jwt}`,
              'Content-Type': 'application/json'
            },
            xhrFields: {
                withCredentials: true
            }
          }
          // Even though the authentication returned a user object that can be
          // decoded, we fetch it again. This way we aren't super dependant on
          // JWT and can plug in something else.
          const axiosInstance = axios.create(base)
          axiosInstance({
            url: "/api/users/",
            method: "get",
            params: {}
          })
            .then((response) => {
              this.$store.commit("setAuthUser",
                {authUser: response.data, isAuthenticated: true}
              )
              this.$router.push({name: 'about'});
              this.$emit("authenticated", true)
            })

        })
        .catch((error) => {
        alert('Wrong username or password!!! If you dont have an Account please create one and log in !!!!');
          console.log(error);
          console.debug(error);
          console.dir(error);
        })
    }
  }
}
</script>

<style scoped>
    @import "./assets/main.css";
</style>
