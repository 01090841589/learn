<template>
  <div>
    <h1>로그인 페이지입니다.</h1>
    <LoginForm/>
  </div>
</template>

<script>
// @는 ./src/ 와 같다.
import LoginForm from '@/components/LoginForm'
export default {
  name: 'Login',
  components: {
    LoginForm,
  }
}
</script>

<style>

</style>