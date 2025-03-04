export default function getListStudents {
  const array = [
    {
      firstName: 'Guillaume',
      id: 1,
      location: 'San Francisco'
    },
    {
      firstName: 'James',
      id: 2,
      location: 'Columbia'
    },
    {
      firstName: 'Serena',
      id: 2,
      location: 'San Francisco'
    }
  ]

  return `id: ${id}, firstName: '${firstName}', location: '${location}'`
}