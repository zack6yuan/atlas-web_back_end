export default class Building {
  constructor(sqft) {
    this.sqft = sqft; // number
  }

  evacuationWarningMessage() {
    return `Class extending Building must override evacuationWarningMessage`
  }

  get sqft() {
    return this._sqft;
  }
}
