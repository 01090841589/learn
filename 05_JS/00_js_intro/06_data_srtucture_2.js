// forEach filter find map every same reduce

// ES5
// var colors = ['red', 'blue', 'green']

// for (var i = 0; i < colors.length; i++){
//   console.log(colors[i])
// }  

// colors.forEach(function(colors) {
//   console.log(colors)

// })

// colors.forEach( color => console.log(color))


// function handlePosts() {

//   const posts = [
//     {id: 23, title: 'Daliy Js News'},
//     {id: 52, title: 'Code Refector City'},
//     {id: 105, title: 'The Brightest Ruby'},
//   ]

//   for (let i = 0; i< posts.length; i++){
//     console.log(posts[i])
//     console.log(posts[i].id)
//     console.log(posts[i].title)

//   }

//   posts.forEach( post => {console.log(post),console.log(post.id),console.log(post.title)})
//   posts.forEach( post => console.log(post)+console.log(post.id)+console.log(post.title))
// }

// handlePosts()

// const images = [
//   { height: 10, width:30},
//   { height: 20, width:90},
//   { height: 45, width:12},
// ]
// const areas = []
// images.forEach(images =>  areas.push(images.height*images.width))
// console.log(areas)

// var numbers = [1, 2, 3]
// var doublenumbers = []

// for (var i=0; i < numbers.length; i++){
//   doublenumbers.push(numbers[i] *2)
// }
// console.log(doublenumbers)

// doublenumbers = numbers.map(function(number){
//   return number *2
// })
// console.log(doublenumbers)

// const numbers = [4, 9, 16]
// const roots = numbers.map(Math.sqrt)
// console.log(roots)


// const images = [
//   { height: '34px', width:'39px'},
//   { height: '54px', width:'19px'},
//   { height: '83px', width:'75px'},
// ]
// const heights = images.map(image => image.height)
// console.log(heights)

// const trips = [
//   { distance: 34, time:10},
//   { distance: 90, time:50},
//   { distance: 59, time:20},
// ]

// const speeds = trips.map(trip => trip.distance/trip.time)
// console.log(speeds)

// const brands = ["Marvel", "DC"]
// const movies = ["IronMan", "Batman"]

// const comics = brands.map((x, i) => ({name: x, hero: movies[i]}))
// console.log(comics)

var products = [
  {name: 'cucumber', type: 'vegetable'},
  {name: 'banana', type: 'fruit'},
  {name: 'carrot', type: 'vegetable'},
  {name: 'apple', type: 'fruit'},

]

// var fruitProducts = []

// for (var i = 0; i < products.length; i++){
//   fruitProducts.push(products[i])
// }
// console.log(fruitProducts)

// const fruitProducts = products.filter(function(product){
//   return product.type === 'fruit'
// })
// console.log(fruitProducts)

// const numbers = [15, 25, 35, 45, 55, 65, 75, 85, 95]

// const gtFifth = numbers.filter( number => number>50)
// console.log(gtFifth)

// const users = [
//   { id: 1, admin: false, name:'justin'},
//   { id: 2, admin: false, name:'harry'},
//   { id: 3, admin: true, name:'tak'},
//   { id: 4, admin: false, name:'jason'},
//   { id: 5, admin: true, name:'juan'},
// ]
// const admin = users.filter(user => user.admin===true)
// console.log(admin[1])

// const ssaftTests = [90, 90, 80, 77]
// const sum = ssaftTests.reduce((total,x) => total += x, 0)
// console.log(sum)

// const arr = [0, 1, 2, 3]
// const totalSum = arr.reduce((total, x) => total += x)
// console.log(totalSum)

// const names = ['harry', 'jason', 'tak', 'tak', 'justin']
// const cntNames = names.reduce(function(allNames, name){
//   console.log(allNames)
//   console.log(name)
//   if (name in allNames){
//     allNames[name]++;
//   }
//   else{
//     allNames[name] = 1
//   }
//   return allNames
// }, {})
// console.log(cntNames)

// var users = [
//   {name: 'Tony', age:23},
//   {name: 'Tony', age:22},
// ]

// for (var i=0; i<users.length; i++){
//   if (users[i].name === 'Tony') {
//     var user = users[i]
//     break
//   }
// }
// console.log(user)

// const user = users.find(user => user.name === 'Tony')
// console.log(user)

// //some 하나이상 / every 모두다 통과하면 True / False
// const arr = [1, 2, 3, 4, 5]
// const result = arr.some(a => a===2)

// console.log(result)


// function conCat (str1, str2){
//   return `${str1} - ${str2}`
// }
// function checkLongStr(string){
//   if (string.length > 10){
//   return true
//   }
//   else{
//     return false
//   }
// }
// if (checkLongStr(conCat('Happy', 'Hacking'))){
//   console.log('LONG STRING')
// }
// else{
//   console.log('SHORT STRING')
// }

const PEOPLE = [
  { id:1, admin:false },
  { id:2, admin:false },
  { id:3, admin:true },
]

let admin = PEOPLE.find(people => people.admin === true)
console.log(admin)
const COMPUTERS = [
  {name : 'macbook', ram: 16},
  {name : 'gram', ram: 8},
  {name : 'series9', ram: 32},
]