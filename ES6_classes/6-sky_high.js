import Building from './5-building';
export default class SkyHighBuilding {
  constructor(sqft, floors) {
    this.sqft = sqft; // number: assigned to parent class Building
    this.floors = floors; // number
  }

  get sqft() {
    return this.sqft;
  }

  get floors() {
    return this.floors;
  }

  // Override the method named evacuationWarningMessage and return
  // the following string Evacuate slowly the NUMBER_OF_FLOORS floors.
}