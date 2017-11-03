function showElementDetails(e) {
  let number = this.getAttribute('data-number')
  let element = window.tableData.elements[number - 1]
  document.querySelector('#cardNumber').innerHTML = element.number
  document.querySelector('#cardSymbol').innerHTML = element.symbol
  document.querySelector('#cardLink').innerHTML = `<a href="${element.link}">github.com/foo/${element.name}</a>`
  document.querySelector('#cardStars').innerHTML = `★ 3992`
  document.querySelector('#cardBlurb').innerHTML = 'A long Blurbie blurb blurb.'

}


function addElementToTable(data, tableDiv) {
  let elDiv = document.createElement('div')
  let symbol = document.createTextNode(data.symbol)
  elDiv.appendChild(symbol)
  elDiv.setAttribute('class', 'table-element')
  elDiv.setAttribute('style', `grid-column:${data.col}; grid-row:${data.row}`)
  elDiv.setAttribute('data-number', data.number)
  tableDiv.appendChild(elDiv)
  elDiv.addEventListener('click', showElementDetails)
}

window.onload = () => {
  let tableDiv = document.querySelector('#periodic-table')

  window.tableData.elements.forEach((e) => {
    addElementToTable({row: e.ypos, col: e.xpos, symbol: e.symbol, number: e.number}, tableDiv)
  })

}
