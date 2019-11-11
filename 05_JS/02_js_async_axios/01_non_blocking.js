const nothing = () => {}

// console.log('start')
// setTimeout(nothing, 3000)
// console.log('end')

// function sleep_3s(){
//   setTimeout(() => {
//     console.log('일어나')

//   }, 3000)
// }

// console.log('start')
// sleep_3s()
// console.log('end')
// sleep_3s()
// console.log('end')
// sleep_3s()
// console.log('end')
// sleep_3s()
// console.log('end')
// sleep_3s()


function first() {
  console.log('first')
}
function second() {
  console.log('second')
}
function third() {
  console.log('third')
}

first()
setTimeout(first, 1000)
setTimeout(second, 500)
setTimeout(third, 0)