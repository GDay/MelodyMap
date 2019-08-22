var fs = require('fs')
fs.rename('../back/static/js/index.html', '../back/adverts/templates/index.html', function (err) {
    if (err) throw err
    console.log('Successfully renamed - AKA moved!')
  })