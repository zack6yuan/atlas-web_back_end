import getListStudents from "./0-get_list_students"

export default function getListStudentIds(array) {
  if (typeof array != 'array') {
    const newArray = []
    return newArray.map(getListStudents)
  }
}
