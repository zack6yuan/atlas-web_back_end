import Building from './5-building';
export default class SkyHighBuilding {
  constructor(sqft, floors) {
    this.sqft = sqft; // number: assigned to parent class Building
    this.floors = floors; // number
  }

  set sqft(sqft) {
    if (typeof sqft !== 'number')
  }
}