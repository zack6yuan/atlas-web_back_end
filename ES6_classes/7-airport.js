export default class Airport {
  constructor(name, code) {
    this._name = name // string
    this._code = code //string
  }

  AirportDetails() {
    return `_name: '${this.name}', _code: '${this.code}'`; // not correct
  }
}
