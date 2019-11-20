<template>
  <div class="todo-input">
    <div class="input-group mb-3" @submit.prevent="createTodo">
      <div class="card-body" d-flex justify-content-between>
        <span>{{todo.title}}</span>
      </div>
    </div>
  </div>
  
</template>

<script>
export default {
  data(){
    
  }
}
</script>

<style>

</style>