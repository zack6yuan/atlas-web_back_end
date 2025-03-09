import getListStudents from "./0-get_list_students"

export default function getListStudentIds(array) {
  if (Array.isArray(array)) {
    const newArray = []
    return newArray.map(getListStudents(array[1]));
  } else {
    throw (new TypeError('not an array'))
  };
}
