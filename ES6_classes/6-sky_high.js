import Building from './5-building';
export default class SkyHighBuilding {
  constructor(sqft, floors) {
    this.sqft = sqft; // number: assigned to parent class Building
    this.floors = floors; // number
  }

  get sqft() {
    return this._sqft;
  }

  get floors() {
    return this._floors;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors.`;
  }
}
