export default class Building {
  constructor(sqft) {
    this._sqft = sqft; // number
  }

class extendingClass extends Building {
  constructor() {
    super(sqft);
  }
  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
};
