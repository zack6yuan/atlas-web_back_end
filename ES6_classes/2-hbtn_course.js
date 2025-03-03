export default class HolbertonCourse {
  /* Attributes
  name: string
  length: number
  students: array of strings */
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  // Setter for name
  set name(name) {
    if (typeof name !== 'string') {
      throw new TypeError("name must be a string");
    }
    this._name = name;
  }

  // Getter for name
  get name() {
    return this._name;
  }

  // Setter for length
  set length(length) {
    if (typeof length !== 'number') {
      throw new TypeError('length must be a number');
    }
    this._length = length;
  }

  // Getter for length
  get length() {
    return this._length;
  }

  // Setter for students
  set students(students) {
    if (!Array.isArray(students)) {
      throw new TypeError('students must be an array of strings');
    }
    this._students = students;
  }

  // Getter for students
  get students() {
    return this._students;
  }
}
