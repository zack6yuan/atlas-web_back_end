export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand; // string
    this._motor = motor; // string
    this._color = color; // string
  }

  cloneCar() {
    return new Car();
  }
  
  // I believe we need to check if the new object
  // of class 'Car' has successfully been created.
}
