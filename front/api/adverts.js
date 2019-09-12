export default (axios, store) => ({
  add (payload) {
    payload.min_age = payload.range[0]
    payload.max_age = payload.range[1]
    return axios.post('/api/listings/', payload).then((response) => {
      return response.data
    }).catch((error) => {
      return Promise.reject(error.response.data)
    })
  },
  search (payload) {
    return axios.post('/api/listings/search', payload).then((response) => {
      return response.data
    }).catch((error) => {
      return Promise.reject(error.response.data)
    })
  },
  sendMesasge (id, payload) {
    return axios.post(`/api/listings/${id}/email`, payload).then((response) => {
      return response.data
    }).catch((error) => {
      return Promise.reject(error.response.data)
    })
  },
  getInstruments () {
    return axios.get('/api/listings/instrument').then((response) => {
      return response.data
    }).catch((error) => {
      return Promise.reject(error.response.data)
    })
  }
})
