<template>
  <div>
    <h1>최상위 컴포넌트</h1>
    <TodoList category="앟"> </TodoList>
    <TodoList category="먼데"> </TodoList>
    <TodoList category="나와라"> </TodoList>
  </div>
</template>


<script>
import TodoList from './components/TodoList.Vue'

export default {
  components: {
    TodoList,
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
  margin-top: 60px;
}
</style>
