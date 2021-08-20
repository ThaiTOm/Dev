// function tra ve gia tri la object
const functionDemp = (a: string, b: number): object => {
    return { a: "duythai" }
}

// array nhan vao gia tri (type) trung voi type truoc do
let arr = ["thai", "123", "123123"]
arr.push("thai ne ")
// arr.push(123123) wrong type

let brr = ["qwe", 123, false]
brr.push("123123")
brr.push(312)
brr.push(true)
// brr.push({a:1})


// declare new variable
let nameme: string = "dythai"
let students: string[] = ["thai", "duyt"]

let mixArr: (string | number | boolean)[]
mixArr[0], mixArr[1], mixArr[2] = 123, "true"
let id: (string | number)

// any types
let age: any = 123
age = "duythai"


