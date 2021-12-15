const fs = require('fs');

var givenpath = process.argv[2]

console.log('Istnieje?', checkExists(givenpath))
console.log('Katalog?', checkIsDir(givenpath))
console.log('Plik?', checkIsFile(givenpath))
console.log('Zawartość?', readFile(givenpath))

if (checkIsFile(givenpath)) {
  fs.readFile(givenpath, 'utf8', (err, data) => {
    console.log('Zawartość?', data)
  })
}

function checkExists(fpath) {
  try {
    if (fs.existsSync(fpath)) {
      return true
    }
    return false
  }
  catch (err) {
    return false
  }
}

function checkIsDir(fpath) {
  if (checkExists(fpath)) {
    if (fs.statSync(fpath).isDirectory()) {
      return true
    } else {
      return false
    }
  } else {
    return false
  }
}

function checkIsFile(fpath) {
  if (checkExists(fpath)) {
    if (fs.statSync(fpath).isFile()) {
      return true
    } else {
      return false
    }
  } else {
    return false
  }
}

function readFile(fpath) {
  if (checkIsFile(fpath)) {
    return fs.readFileSync(fpath, {encoding:'utf8'})
  }
  else {
    return null
  }
}

exports.checkExists = checkExists
exports.checkIsDir = checkIsDir
exports.checkIsFile = checkIsFile
exports.readFile = readFile
