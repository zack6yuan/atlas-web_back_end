export default class Building {
  constructor(sqft) {
    this.sqft = sqft; // number
  }

  set sqft(sqft) {
    if (typeof sqft !== 'number') {
      throw new TypeError('sqft must be a number')
    }
    this.sqft = sqft;
  }

  get sqft() {
    return this.sqft;
  }
}