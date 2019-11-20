<template>
  <div class="todo-list">
    <div class="card" v-for="todo in todos" :key="todo.id">

      <div class="card-body" d-flex justify-content-between>
          <span @click="updateTodo(todo)">{{todo.title}}<span>
          <span @click="deleteTodo(todo)">{{todo.title}}</span>
        </span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  
  methods: {
    deleteTodo(todo) {
      this.$session.start()
      const token = this.$session.get('jwt')
      const requestHeader = {
        headers: {
          Authorization: 'JWT '+token
        }
    }
    axios.post(`http://127.0.0.1:8000/api/v1/todos/`,requestForm, requestHeader)
    .then(res => {
      console.log(res)
      this.targetTodo = this.todos.find(function(el) {

      })
    })
    .catch(err => {
      console.log(err)
    })
  },
  updateTodo(todo){
    this.$session.start()
    const token = this.$session.get('jwt')
    const requestHeader = {
      headers: {
        Authorization: 'JWT '+token
      }
    }
    const requestForm = new FormData()
    requestForm.append('completed', !todo.completed)
    requestForm.append('user', !todo.user)
    requestForm.append('id', !todo.id)
    requestForm.append('title', !todo.title)
    console.log(!todo.completed, todo.user, todo.id, todi.title)

    axios.put(`http://127.0.0.1:8000/api/v1/todos/${todo.id}`,requestForm, requestHeader)
    .then(res => {
      this.todos.push(res.data)
      console.log(res)
    })
    .catch(err => {
      console.log(err)
    })
  }
}
</script>

<style>

</style>