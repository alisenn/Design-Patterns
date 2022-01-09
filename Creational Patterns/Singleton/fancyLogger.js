class FancyLogger {
    constructor() {
        if (FancyLogger.instance == null){
            this.logs = []
            FancyLogger.instance = this  //lazy instantiation
        }
        return  FancyLogger.instance
    }
    log(message) {
        this.logs.push(message)
        console.log(`FANCY: ${message}`)
    }

    printLogCount(){
        console.log(`${this.logs.length} Logs`)
    }

}


const logger = new FancyLogger()
Object.freeze(logger)
export default logger