<template>
  <div id="app">
    <button @click="gpost" >Get Posts</button>
    <li v-for="data in datas" :key="data">
      {{data.title}} - {{data.body}}


    </li>
  </div>
</template>

<script>

import axios from 'axios'

export default {
  name: 'app',
  components: {
  },
  data() {
    return{
      datas: [],
    }
  },
  methods: {
    gpost(){
      axios.get('https://jsonplaceholder.typicode.com/posts')
      .then(res => {
        this.datas = res.data
    })
  }
}
}
</script>

<style>
</style>
