import getListStudents from "./0-get_list_students"

export default function getListStudentIds(objectsArray) {
  /* eslint-disable no-unused-vars */
  // if not an array, return an empty array
  if (!Array.isArray(objectsArray)) {
    return [];
  }
  // use map function
  return objectsArray.map(obj => (obj.id));
}
