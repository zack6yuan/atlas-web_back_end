export default function getListStudentIds(array) {
  if (typeof array != 'array') {
    const newArray = []
    return newArray.map(getListStudentIds)
  }
}
