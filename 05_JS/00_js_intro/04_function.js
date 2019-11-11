// function add(num1, num2){
//   return num1+num2
// }

// console.log(add(2, 7))


// const sub = function(num1, num2){
//   return num1-num2
// }
// console.log(sub(2, 7))


//Arrow function
//function keyword 생략 가능
// 함수의 매개변수가 1개라면 () 생략 가능
// 함수 바디의 표현식이 하나라면 {} 와 return 생략 가능

//함수 표현식
// const ssafy1 = function() {
//   return 'Hello!'
// }

// const ssafy2 = (name) => { return `Hello! ${name}`}
// console.log(ssafy2('wer'))

//()생략할 수 있다.(인자가 1개 있을때)
// const ssafy2 = name => { return `Hello! ${name}`}
// console.log(ssafy2('wer'))

// {} 와 return 생략
// const ssafy2 = name => `Hello! ${name}`
// console.log(ssafy2('wer'))


// // let square = function(num){
// //   return num ** 2
// // }
// let square0 = (num) => {return `${num**2}` }
// console.log(square0(2))

// let square1 = num => {return `${num**2}` }
// console.log(square1(2))

// let square2 = num => `${num**2}`
// console.log(square2(2))

// let square3 = num => num**2
// console.log(square3(2))


// let noArgs = () => 'NoArgs'
// console.log(noArgs())
// let noArgs1 = _ => 'NoArgs'
// console.log(noArgs1())
// let returnObject = _ => ({ key : 'value'})
// console.log(returnObject())

// const sayHello = (name='noName') => `hi ${name}`

//익명 함수
//즉시 실행 함수는 초기화에 많이 사용

// function (num) {return num**3}

//1.기명함슈
// const cube = function (num) {return num**3}
// const squareRoot = num => num ** 0.5

// console.log(cube(2))
// console.log(squareRoot(4))

// console.log((function (num) {return num ** 3 })(2))
// console.log((num => num ** 0.5)(2))

// 함수우우

// let ssafy2 = function () {
//   console.log('asdf')

// }

var ssafy3

ssafy3()

ssafy3() = function(){
  console.log('asdf')
}