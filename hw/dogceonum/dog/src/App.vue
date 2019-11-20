<template>
  <div id="app">
    <h1>사진 몇개</h1>
    <select v-model="nums" name="sel" id="sel">
      <option v-for="number in numbers" :value="number" :key=number>{{number}}</option>
    </select>
    <button @click="getdog">Get {{nums}} Dog</button>
    <img v-for="dogimage in dogimages" :src="dogimage" :key="dogimage">
    {{dogimages}}
  </div>
</template>

<script>
import axios from 'axios'



export default {
  name: 'app',
  components: {
  },
  data() {
    return {
      dogimages : '',
      nums: 1	,
      numbers: 9,
    }
  },
  methods: {
    getdog(){
      axios.get(`https://dog.ceo/api/breeds/image/random/${this.nums}`)
      .then(res => {
        this.dogimages = res.data.message
      })
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
  margin-top: 60px;
}
</style>
