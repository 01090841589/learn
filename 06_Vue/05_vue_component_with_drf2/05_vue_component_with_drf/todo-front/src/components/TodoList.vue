<template>
  <div class="todo-list">
    <div class="card" v-for="todo in todos" :key="todo.id">
      <div class="card-body" d-flex justify-content-between>
        <span @click="updateTodo(todo)" :class="{complete: todo.completed}">{{ todo.title }}</span>
        <span @click="deleteTodo(todo)">💣</span>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'TodoList',
  props: {
    todos:{
      type: Array,
      required: true,
    }
  },
  methods:{
    deleteTodo(todo){
      this.$session.start()
      const token = this.$session.get('jwt')
      const requestHeader = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      axios.delete(`http://127.0.0.1:8000/api/v1/todos/${todo.id}/`, requestHeader)
      .then(res =>{
        console.log(res)
        const targetTodo = this.todos.find(function(el){
          return el === todo
        })
        const idx = this.todos.indexOf(targetTodo)
        if (idx>-1){
          // .splice(idx, N)는 리스트의 idx 인덱스부터 N개 지우겠다는 의미
          this.todos.splice(idx, 1)
        }
      })
      .catch(err =>{
        console.log(err)
      })
    },
    updateTodo(todo){
      this.$session.start()
      const token = this.$session.get('jwt')
      const requestHeader = {
        headers:{
          Authorization: 'JWT ' + token
        }
      }
      const requestForm = new FormData()
      requestForm.append('completed', !todo.completed)
      requestForm.append('user', todo.user)
      requestForm.append('id', todo.id)
      requestForm.append('title', !todo.title)
      console.log(!todo.completed, todo.user, todo.id, !todo.title)
      axios.put(`http://127.0.0.1:8000/api/v1/todos/${todo.id}/`, requestForm, requestHeader)
      .then(res =>{
        console.log(res)
        todo.completed = !todo.completed
      })
      .catch(err=>{
        console.log(err)
      })
    }
  }

}
</script>

<style>
  .complete{
    text-decoration: line-through;
    color : rgb(112, 112, 112)
  }
</style>