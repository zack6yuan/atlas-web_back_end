export default function getListStudentIds(array) {
  if (!Array.isArray(array)) {
    newArray = [];
    return newArray;
  }
  const array = [
    {
      firstName: 'Guillaume',
      id: 1,
      location: 'San Francisco',
    },
    {
      firstName: 'James',
      id: 2,
      location: 'Columbia',
    },
    {
      firstName: 'Serena',
      id: 5,
      location: 'San Francisco',
    },
  ];
  const arrayIds = array.map((id) => `${id}`
  )
}
