// type Alias
type StringStudent = string | number
type Student = {
    name: string,
    age: number
}

let fnc = (student: Student): string => {
    return `${student.name} la ten`
}
fnc({ name: "Duythai", age: 0 })


let func: (a: number, b: number) => number
func = (num1: number, num2: number) => {
    return 123123
}
func(123, 312)

// without require 
const funDe = (name: string, age?: number) => name