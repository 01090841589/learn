import jwtDecode from 'jwt-token'

const state = {
  token: null,
  loading: false
}
const getters = {
  isLoggedIn: function(state) {
    return state.token ? true : false
  },
  requestHeader: function(state) {
    return {
      headers: {
        Authorization: 'JWT '+ state.token
      }
    }
  },
  userId: function(state) {
    return state.token ? jwtDecode(state.token).user_id : null
  }
}
const mutations = {
  setToken: function(state, token) {
    state.token = token
  },
  setLoading: function(state, status) {
    state.loading = status
  }
}
const actions = {
  login: function(context, token) {
    context.commit('setToken', token)
  },
  logout: function(context) {
    context.commit('setToken', null)
  },
  startLoading: function(context) {
    context.commit('setLoading', true)
  },
  endLoading: function(context) {
    context.commit('setLoading', false)
  },
  
}

export default {
  state,
  getters,
  mutations,
  actions,
}