
// // //var로 선언된 변수의 범위는 현재 실행 문맥 -> 함수 or 함수 외주 전역
// // // var x = 1

// // // var visited = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


// if (true){
//   var x = 2
//   console.log(x)
// }
// console.log(x)
// console.log(visited)

// // // let -> 값을 재할당 할 수 있는 선언 키워드(선언은 한번만, 할당은 여러번 가능)
// // // let x = 1
// // // console.log(x)
// // // x = 2
// // // console.log(x)


// let x = 1;

// if (x === 1){
//   let x = 2
//   console.log(x)
// }
// console.log(x)

// // // const ->  상수, 값이 변하지 않는 상수를 선언

// // // const MY_FAV = 7
// // // console.log(MY_FAV)


// // // let과 var의 스코프 비교

// // //var

// // // function varTest(){
// // //   var x = 1
// // //   if (true){
// // //     var x = 2
// // //     console.log(x)
// // //   }
// // //   console.log(x)
// // // }
// // // varTest()

// // //let

// function varTest(){
//   let x = 1
//   if (true){
//     let x = 2
//     console.log(x)
//   }
//   console.log(x)
// }
// varTest()


// // // var a = 1
// // // var b = 2
// // // if (a === 1){
// // //   var a = 11
// // //   let b = 22
// // //   console.log(a)
// // //   console.log(b)
// // // }
// // // console.log(a)
// // // console.log(b)

// // //var : 할당 및 선언 자유 , 함수 스코프
// // //let : 할당 자유 선언은 한번만, 블록 스코프
// // //const : 할당 및 선언 한번만, 블록 스코프

// // // 변수와 식별자 - 식별자
// // // 객체, 변수, 함수 -> 카멜 케이스(lower-camel-case)

// // // 숫자 문자 불리언
// // let dog
// // let variableName

// // //객체
// // const memberInfo = {
// //   id: 1,
// //   password: 12345,
// //   gender: 'male',
// // }

// // // 배열 - 배열은 보통 복수형을 사용
// // const dogs = []

// // // 정규표현식 - 'r' 로 시작
// // const rDesc = /ab+c/

// // // 함수
// // function getPropertyName(){

// // }

// // //이벤트 핸들러 - 이벤트 핸들러는 'on'으로 시작
// // const onClick = () => {}
// // const onKeyDown = () => {}

// // // boolean을 반환하는 함수 -> return 값이 불리언인 함수는 'is'로 시작
// // let isAvaliable = false

// // //파스칼 케이스(Upper-camel-case) - 클래스생성자

// class User {
//   constructor(options){
//     this.name = options.name
//   }
// }

// const good = new User ({
//   name: 'yup',

// })
// console.log(good)
// console.log(typeof good)

// // 대문자 스네이크 케이스 - 상수

// export const API_KEY  = 'SOMEKEY'

// export const MAPPING = {
//   key = 'value'
// }
