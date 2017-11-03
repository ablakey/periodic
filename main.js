function showElementDetails(e) {
  let number = this.getAttribute('data-number')
  let element = window.tableData[number - 1]
  let url = element.url.replace('https://api.github.com/repos/', 'http://github.com/')
  let urlLabel = url.replace('http://github.com/', '')
  document.querySelector('#cardNumber').innerHTML = element.number
  document.querySelector('#cardSymbol').innerHTML = element.symbol
  document.querySelector('#cardLink').innerHTML = `<a href="${url}">github.com/${urlLabel}</a>`
  document.querySelector('#cardStars').innerHTML = `★ ${element.stars}`
  document.querySelector('#cardBlurb').innerHTML = element.description
}

function getStarRank(count) {
  return Math.floor(Math.max(count, 1000) / 200)
}

const colors = {
  0: '#fff',
  1: '#eee',
  2: '#c6e48b',
  3: '#7bc96f',
  4: '#239a3b',
  5: '#196127'
}

function addElementToTable(data, tableDiv) {
  let elDiv = document.createElement('div')
  let symbol = document.createTextNode(data.symbol)

  let bgColor = colors[getStarRank(data.stars)]

  elDiv.appendChild(symbol)
  elDiv.setAttribute('class', 'table-element')
  elDiv.setAttribute('style', `grid-column:${data.col}; grid-row:${data.row} background-color:${bgColor}`)
  elDiv.setAttribute('data-number', data.number)
  tableDiv.appendChild(elDiv)
  elDiv.addEventListener('click', showElementDetails)
}

window.onload = () => {
  let tableDiv = document.querySelector('#periodic-table')

  window.tableData.forEach((e) => {
    addElementToTable({row: e.row, col: e.col, symbol: e.symbol, number: e.number}, tableDiv)
  })
}
