<template>
  <div id="app" class="container">
    <div id="nav">
      <!-- <div v-if="isAuthenticated"> -->
      <div v-if="isLoggedIn">

        <!-- 라우터 지원 앱에서 사용자 네비게이션을 가능하게 하는 컴포넌트.
        목표 위치는 to로 지정 -->
        <router-link to="/">Home</router-link> |
        <a @click.prevent="logout" href="#">Logout</a>
      </div>
      <div v-else>
        <router-link to="/login">Login</router-link> |
        <router-link to="/register">Register</router-link>
      </div>
    </div>
    <!-- 특정 라우팅 경로에 맞는 컴포넌트가 렌더되는 자리 -->
    <div class="row justify-content-center">
      <router-view class="col-6"/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  // data(){
  //   return {
  //     isAuthenticated: this.$session.has('jwt')
  //   }
  // },
  // updated(){
  //   this.isAuthenticated = this.$session.has('jwt')
  // },
  computed:{
    isLoggedIn: function(){
      return this.$store.getters.isLoggedIn
    }
  },
  
  methods:{
    logout(){
      // this.$session.destroy()
      this.$store.dispatch('logout')

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
