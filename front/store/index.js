export const state = () => ({
  token: '',
  snackbarText: '',
  snackbar: false,
  loginModalOpen: false,
  signupModalOpen: false,
  center: [47.413220, -1.219482],
  zoom: 3
})

export const mutations = {
  setCSRFToken (state, token) {
    state.token = token
  },
  setZoom (state, zoom) {
    state.zoom = zoom
  },
  setSnackbar (state, text) {
    state.snackbarText = text
    state.snackbar = !state.snackbar
  },
  toggleSignupModal (state) {
    state.signupModalOpen = !state.signupModalOpen
  },
  toggleLoginModal (state) {
    state.loginModalOpen = !state.loginModalOpen
  },
  changePlace (state, place) {
    state.center = [place.lat, place.lon]
    state.zoom = 11
  }
}

export const actions = {
  showSnackbar ({ state, commit }, text) {
    commit('setSnackbar', text)
    if (!state.snackbar) {
      setTimeout(() => {
        commit('setSnackbar', text)
      }, 100)
    }
  }
}
