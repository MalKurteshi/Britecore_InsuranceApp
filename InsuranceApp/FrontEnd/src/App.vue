<template>
  <div id="app">
    <b-navbar toggleable="md" type="dark" variant="info" v-if="authenticated">
      <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
      <b-navbar-brand href="#">Britecore</b-navbar-brand>
      <b-collapse is-nav id="nav_collapse">
        <b-navbar-nav>
          <b-nav-item href="#"> <router-link to="/policies">Make Policy </router-link></b-nav-item>
          <b-nav-item href="#"> <router-link to="/ShowPolicies">Show Policies</router-link></b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-item-dropdown right>

            <!-- Using button-content slot -->
            <template slot="button-content">
              <em>User</em>
            </template>
            <b-dropdown-item href="#"><router-link v-if="authenticated" to="/login" v-on:click.native="logout()" replace>Signout</router-link></b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>

      </b-collapse>
    </b-navbar>

    <router-view  @authenticated="setAuthenticated"/>

  </div>
</template>
<script>
export default {
  name: 'App',
  data() {
    return {
      authenticated: false,

    }
  },
  mounted() {
    if(!this.authenticated) {
      this.$router.replace({ name: "login" });
    }
  },
  methods: {
    setAuthenticated(status) {
      this.authenticated = status;
    },
    logout() {
      this.authenticated = false;
      this.$session.destroy()
    }
  }
}
</script>

<style>
  @import "views/assets/bootstrap.min.css";
</style>
