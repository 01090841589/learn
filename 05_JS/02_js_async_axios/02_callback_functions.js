// // 올 덧셈
// const numbersAddEach = numbers => {
//   let sum = 0
//   for (const number of numbers){
//     sum += number
//   }
//   return sum
// }
// console.log(numbersAddEach([1, 2, 3, 4, 5]))


// // 올 뺼셈
// const numbersSubEach = numbers => {
//   let sum = 0
//   for (const number of numbers){
//     sum -= number
//   }
//   return sum
// }
// console.log(numbersSubEach([1, 2, 3, 4, 5]))

// // 올 곱셈
// const numbersMulEach = numbers => {
//   let sum = 1
//   for (const number of numbers){
//     sum *= number
//   }
//   return sum
// }
// console.log(numbersMulEach([1, 2, 3, 4, 5]))

// const NUMBERS = [1, 2, 3, 4, 5]

// const numbersEach = (numbers, callback) => {
//   let acc
//   for (const number of numbers){
//     acc = callback(number, acc)
//   }
//   return acc
// }
// const addEach = (number, acc=0) => {
//   return acc+number
// }
// console.log(numbersEach(NUMBERS, addEach))
// const subEach = (number, acc=0) => {
//   return acc-number
// }
// console.log(numbersEach(NUMBERS, subEach))
// const mulEach = (number, acc=1) => {
//   return acc*number
// }
// console.log(numbersEach(NUMBERS, mulEach))



const NUMBERS = [1, 2, 3, 4, 5]

const numbersEach = (numbers, callback) => {
  let acc
  for (const number of numbers){
    acc = callback(number, acc)
  }
  return acc
}

console.log(numbersEach(NUMBERS, (number, acc=0) => acc+number))
console.log(numbersEach(NUMBERS, (number, acc=0) => acc-number))
console.log(numbersEach(NUMBERS, (number, acc=1) => acc*number))