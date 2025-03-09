export default function getListStudentIds(array) {
  if (!Array.isArray(array)) {
    newArray = [];
    return newArray;
  }

  const arrayIds = array.map((id) => `${id}`
  )
}
