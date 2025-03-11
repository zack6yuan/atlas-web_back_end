export default class Building {
  constructor(sqft) {
    this.sqft = sqft; // number
  }

  get sqft() {
    return this.sqft;
  }

  if (evacuationWarningMessage not instanceof Building) {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }

  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
