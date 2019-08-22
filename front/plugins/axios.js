import Cookies from 'js-cookie'
import user from '~/api/user'
import adverts from '~/api/adverts'

export default function ({ store, $axios, redirect }, inject) {
  $axios.interceptors.request.use(
    function (config) {
      config.headers['x-csrftoken'] = store.state.token
      delete config.headers.common.Authorization
      return config
    },
    function (error) {
      return Promise.reject(error)
    }
  )
  $axios.interceptors.response.use(
    function (response) {
      if (Cookies.get('csrftoken') !== undefined && Cookies.get('csrftoken') !== '') {
        store.commit('setCSRFToken', Cookies.get('csrftoken'))
      }
      return response
    },
    function (error) {
      return Promise.reject(error)
    }
  )
  const r = user($axios, store)
  inject('user', r)
  const a = adverts($axios, store)
  inject('adverts', a)
}
