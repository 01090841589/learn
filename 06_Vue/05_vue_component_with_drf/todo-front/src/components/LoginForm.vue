<template>
  <div class="login-div">
    <div v-if="loading" class="spinner-border" role="status">
      <span class="sr-only">Loading..,.,.,.,.,.,..,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,..,.,.,.,..,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,..,.,...,..,.</span>
    </div>
    <div v-else class="login-form" @submit.prevent="login">
      <div v-if="errors.length" class="error-list alert alert-danger">
        <h4>다음의 오류를 해결해주세요</h4>
        <hr>
        <div v-for="(error, idx) in errors" :key="idx">
          {{error}}
        </div>
      </div>
      <div class="form-group">
        <label for="id">ID</label>
        <input 
        type="text" 
        class="form-control" 
        id="id" 
        placeholder="아이디"
        @keyup.enter="login"
        v-model="credentials.username">
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input 
        type="password" 
        class="form-control" 
        id="password" 
        placeholder="비밀번호"
        v-model="credentials.password"
        @keyup.enter="login"
        >
      </div>
      <button class="btn btn-primary" @click="login">로그인</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import router from '../router'

export default {
  name: 'LoginForm',
  data() {
    return {
      credentials: {
        username: '',
        password: '',
      },
      loading: false,
      errors: [],

    }
  },
  computed: {
    loading: function() {
      return this.$store.state.loading
    }
  },
  methods:{
    login() {
      if (this.checkForm()) {
        this.$store.dispatch('startLoading')
        this.loading = true
        axios.post('http://127.0.0.1:8000/api-token-auth/', this.credentials)
        .then(res => {
          this.$store.dispatch('endLoading')
          this.$session.set('jwt',res.data.token)
          router.push('/')
          this.loading = false
          console.log(res)
        })
        .catch (err=> {
          this.loading = false
          console.log(err)
        })
      } else {
        console.log('로그인 실패')
      }
    },
    checkForm() {
      this.errors = []
      if (!this.credentials.username) {
        this.errors.push("아이디를 입력해주세요.")
      }
      if (this.credentials.password.length < 4) {
        this.errors.push("비밀번호는 4글자 이상.")
      }
      if (this.errors.length === 0){
        return true
      }
    }

  }
}
</script>

<style>

</style>