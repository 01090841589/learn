// 1. 변수에 담을수있다
//2. 인자로 전달할수 있다.
//3. 반환값으로 전달할수 있다.

const fco = function () { //1

  return n => n + 1 //3
}
console.log(fco) //2

const num_101 = fco()(100)
console.log(num_101) //2


