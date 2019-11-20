import jwtDecode from 'jwt-decode'

// 상태 정보
const state = {
  token: null,
  loading: false,
}

// getters는 status를 변경하지 않음.
// status를 인자로 받아서 사용
const getters = {
  isLoggedIn: function(state){
    return state.token ? true:false
  },
  requestHeader: function(state){
    return{
      headers:{
        Authorization: 'JWT ' + state.token
      }
    }
  },
  userId: function(state){
    return state.token ? jwtDecode(state.token).user_id : null
  }
}

// 상태(토큰)을 받아와서 변경
// mutation을 통해 state(상태, 데이터)를 변경
const mutations = {
  setToken: function(state, token){
    state.token = token
  },
  setLoading: function(state, status){
    state.loading = status
  }
}

// 로그인/로그아웃
const actions = {
  login: function(context, token){
    context.commit('setToken', token)
  },
  logout: function(context){
    context.commit('setToken', null)
  },
  startLoading: function(context){
    context.commit('setLoading', true)
  },
  endLoading: function(context){
    context.commit('setLoading', false)
  }
}

export default{
  state,
  getters, 
  mutations,
  actions,
}