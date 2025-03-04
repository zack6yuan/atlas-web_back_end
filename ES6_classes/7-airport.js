export default class Airport {
  constructor(name, code) {
    this.name = name // string
    this.code = code //string
  }

  AirportDetails() {
    return `_name: '${this.name}', _code: '${this.code}'`; // not correct
  }
}
