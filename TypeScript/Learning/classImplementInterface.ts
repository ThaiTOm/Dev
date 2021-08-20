import { hasPrint } from "./interFaceForClass";

export class Invoice implements hasPrint {
    constructor(
        readonly client: string,
        private job: string,
        public amount: number
    ) { }
    print() {
        return "duythai"
    }

}