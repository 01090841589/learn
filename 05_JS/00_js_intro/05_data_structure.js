const numbers = [1, 2, 3, 4]

// console.log(numbers[0])
//push pop

// console.log(numbers.unshift('a'))
// console.log(numbers)
// console.log(numbers.shift())
// console.log(numbers)

// console.log(numbers.includes(1))
// console.log(numbers.includes(0))
// console.log(numbers.push('a'))

// console.log(numbers)
// console.log(numbers.indexOf('a'))
// console.log(numbers.indexOf('b'))

// console.log(numbers.join(''))

const me = {
  name: 'ssafy', 
  'phone number': '01012345678',
  appleProducts: {
    ipad: '2019pro',
    iphone: '6s+',
    macbook: '2018pro'
  }

}

// console.log(me.name)
// console.log(me['name'])
console.log(me['phone number'])
console.log(me.phone number)

// console.log(me.appleProducts.ipad)


// const books = ['sadf', 'asdff']

// const movies = {
//   'Horror': ['곤', '겟'],
//   'SF': ['인', '마', '그']
// }

// const magazines = null

// const bookShop = {
//   books: books,
//   movies: movies,
//   magazines:magazines,
// }

// console.log(bookShop)
// console.log(bookShop.books[0])


// ES6+

// const books = ['sadf', 'asdff']

// const movies = {
//   'Horror': ['곤', '겟'],
//   'SF': ['인', '마', '그']
// }

// const magazines = null

// const bookShop = {
//   books,
//   movies,
//   magazines,
// }

// console.log(bookShop)
// console.log(bookShop.books[0])

//JSON <-> object

const jsonData = JSON.stringify({
  coffee: 'ame',
  iceCream: 'c&c'
})
console.log(jsonData)
console.log(typeof jsonData)

const parseData = JSON.parse(jsonData)

console.log(parseData)
console.log(typeof parseData)