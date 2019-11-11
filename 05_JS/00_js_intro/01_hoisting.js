// 나중에 선언한 함수를 참조 할 수 있음

// console.log(a)
// var a = 10
// console.log(a)

// console.log(b)
// let b = 10
// console.log(b)

// var할당 과정
// 1. 선언 - 초기화 (동시에 진행) --> 처음에는 값이 없기 때문에 JS가 undefined를 할당
// 2. 값을 할당 진행
// let할당 과정
// 1. 선언 - 초기화 x 
// 2. TDZ(Temporal Dead Zone) -> 임시적 사각지대
// 3. 초기화(처음에는 값이 없기 때문에 JS가 undefined를 할당) 
// 4. 할당

// let foo
// let bar = undefined

// console.log(foo)
// console.log(bar)


if (x !== 1){
  console.log(y)
  var y = 3
  if (y === 3){
    let x = 1
  }
  console.log(y)
}

if (x === 1){
  console.log(y)
}
x = 7
console.log(x)