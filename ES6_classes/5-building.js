export default class Building {
  constructor(sqft) {
    this.sqft = sqft; // number
  }

  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
