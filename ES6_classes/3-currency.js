export default class Currency {
  constructor(code, name) {
    this.code = code; // string
    this.name = name; // string
  }

  // Setter for code
  set code(code) {
    if (typeof code !== 'string') {
      throw new TypeError('code must be a string');
    }
    this._code = code;
  }

  // Getter for code
  get code() {
    return this._code;
  }

  // Setter for name
  set name(name) {
    if (typeof name !== 'string') {
      throw new TypeError('name must be a string');
    }
    this._name = name;
  }

  // Getter for name
  get name() {
    return this._name;
  }

  displayFullCurrency(name, code) {
    return `${name} (${code})`;
  }
}
