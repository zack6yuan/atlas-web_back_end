export default class Building {
  constructor(sqft) {
    this.sqft = sqft; // number
  }

  evacuationWarningMessage() {
    return `Class extending Building must override evacuationWarningMessage`
  }

  set sqft(sqft) {
    if (typeof sqft !== 'number') {
      throw new TypeError('sqft must be a number');
    }
    this.sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }
}
