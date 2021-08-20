interface person {
    name: string,
    age: number,
    speak(lang: string): boolean
    spend(money: number): string
}

const Thai: person = {
    name: "dythai",
    age: 123,
    speak(value: string) {
        return true ? value == 'VN' : false
    },
    spend(vale: number) {
        return "rich"
    }
}

// declare new function 
const helloPerson = (per: person) => {
    console.log(per)
}
helloPerson(Thai)