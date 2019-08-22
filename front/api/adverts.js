export default (axios, store) => ({
  add (payload) {
    payload.min_age = payload.range[0]
    payload.max_age = payload.range[1]
    return axios.post('/api/adverts/', payload).then((response) => {
      return response.data
    }).catch((error) => {
      return Promise.reject(error.response.data)
    })
  },
  search (payload) {
    return axios.post('/api/adverts/search', payload).then((response) => {
      return response.data
    }).catch((error) => {
      return Promise.reject(error.response.data)
    })
  },
  sendMesasge (id, payload) {
    return axios.post(`/api/adverts/${id}/email`, payload).then((response) => {
      return response.data
    }).catch((error) => {
      return Promise.reject(error.response.data)
    })
  },
  getInstruments () {
    return axios.get('/api/adverts/instrument').then((response) => {
      return response.data
    }).catch((error) => {
      return Promise.reject(error.response.data)
    })
  }
})
