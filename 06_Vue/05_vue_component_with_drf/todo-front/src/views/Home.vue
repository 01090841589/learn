<template>
  <div class="home">
    <h1>Todo with Django</h1>
    <TodoList :todos="todos"/>
  </div>
</template>

<script>
import router from '../router'
import TodoList from '@/components/TodoList'

import axios from 'axios'
import jwtDecode from 'jwt-decode'
import { mapGetters } from 'vuex'
export default {
  name: 'home',
  components: {
    TodoList,
  },
  data() {
    return {
      todos: []
    }
  },
  computed: {
    ...mapGetters([
      'isLoggedIn',
      'requestHeader',
      'userId'
    ])
  },
  methods: {
    checkLoggedIn() {
      if (!this.isLoggedIn){
        router.push('/login')
      }
    },
    getTodos() {
      this.$session.start()
      const token = this.$session.get('jwt')
      console.log(token)
      const requestHeader = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      const user_id = jwtDecode(token).user_id
      console.log(jwtDecode(token))
      axios.get(`http://127.0.0.1:8000/api/v1/users/${this.user_id}/`, this.requestHeader)
      .then(res => {
        console.log(res)
      })
      .catch(err => {
        console.log(err)
      })
    },
    createTodo(title){
      this.$session.start()
      const token = this.$session.get('jwt')
      const requestHeader = {
        headers: {
          Authorization: 'JWT '+token
        }
      }
      const user_id = jwtDecode(token).user_id
      const requestForm = new FormData()
      requestForm.append('user',user_id)
      requestForm.append('title', title)

      axios.post(`http://127.0.0.1:8000/api/v1/todos/`,requestForm, requestHeader)
      .then(res => {
        this.todos.push(res.data)
        console.log(res)
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  mounted() {
    this.checkLoggedIn(),
    this.getTodos()
  }
}
</script>
