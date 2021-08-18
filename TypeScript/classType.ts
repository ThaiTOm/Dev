class StudentClass {
    // truy cap duoc thay doi duoc
    public name: string
    // khong truy cap cung khong thay doi duoc
    private age: number
    // truy cap douc nhung khong thay doi duoc
    readonly male: boolean
    constructor(n: string, a: number, m: boolean) {
        this.name = n
        this.age = a
        this.male = m
    }
    func() {
        return `Hello my name is ${this.name}. ${this.age} and i am ${this.male}`
    }
}
const hendry = new StudentClass("hendry", 123, true)

var thai: string = hendry.name
hendry.name = "Duythai"
// can not change
// hendry.male = true

// Cach khai bao khac
class Employee {
    constructor(
        public name: string,
        private age: number,
        readonly gender: string
    ) { }
}
let bob = new Employee("duythai", 17, "male")
let employArr: Employee[] = []
employArr.push(bob)

