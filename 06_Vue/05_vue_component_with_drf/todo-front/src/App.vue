<template>

  <div id="app">
    <div id="nav">
      <div v-if="isAuthenticated">

        <router-link to="/">Home</router-link> |
        <a @click.prevent="logout" href="#">Logout</a>
      </div>
    </div>
    <div>
      <router-link to="/login">Login</router-link>
    </div>
    <div class="row justify-content-center">
      <div class="container col-6">
    </div>
      <router-view/>
    </div>
  </div>
</template>
<script>
export default {
  name: 'App',
  computed: {
    
  },
  methods: {
    logout() {
      this.$session.destroy()
      this.$router.push('/login')
    }
  }
}

</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
