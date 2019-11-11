<template>
  <div class="container">
    <search-bar @inputChange="onInputChange"></search-bar>
    <div class="row">
      <video-detail :video="selectedVideo"></video-detail>
      <video-list @videoSelect="onVideoSelect" :videos="videos"></video-list>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import SearchBar from "./components/SearchBar"
import VideoList from "./components/VideoList"
import VideoDetail from "./components/VideoDetail"


const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'
export default {
  name: 'app',
  data() {
    return {
      videos: [],
      selectedVideo: null,
    }
  },
  components:{
    SearchBar,
    VideoList,
    VideoDetail
  },
  methods: {
    onVideoSelect(video){
      console.log(video)
      this.selectedVideo = video
    },
    onInputChange(inputValue) {
      axios.get(API_URL, {
        params: {
          key : API_KEY,
          type: 'video',
          part: 'snippet',
          q: inputValue
        }
      })
      .then(response => {
        console.log(response)
        this.videos = response.data.items
      })
      .catch(error => {
        console.log(error)
      })
    }
  }
}
</script>

<style scoped>

input {
  width: 75%;
}
div {
  text-align: center;
  margin:20px
}
</style>
