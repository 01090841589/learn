<template>

  <li class="list-group">
    <div class="media-body">

    <img @click="onVideoSelect" :src="thumbnailUrl" class="mr-3" alt="youtube-thumbnail-image">
    {{ video.snippet.title }}
    </div>
  </li>
</template>

<script>
export default {
  name: 'VideoListItem',
  props: {
    video: {
      type: Object,
      required: true,
    }
  },
  computed: {
    thumbnailUrl() {
      return this.video.snippet.thumbnails.default.url
    }
  },
  methods: {
    onVideoSelect() {
      this.$emit('videoSelect', this.video)


    }
  }
}
</script>

<style scoped>
li {
  display: flex;
  cursor: pointer;
}
li:hover {
  background-color: #eee; 
}
</style>