export default (axios, store) => ({
  getCSRFToken () {
    return axios.get('/api/auth/CSRFtoken').then((response) => {
      return response.data
    }).catch((error) => {
      return Promise.reject(error.response.data)
    })
  },
  signup (payload) {
    return axios.post('/api/auth/signup', payload).then((response) => {
      return response.data
    }).catch((error) => {
      return Promise.reject(error.response.data)
    })
  }
})
