export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand; // string
    this._motor = motor; // string
    this._color = color; // string
  }

  cloneCar() {
    return new Car();
  }
}
