export default function createReportObject(employeesList) {
  const object = {};
  const objectKey = "allEmployees";
  object.objectKey = employeesList;

  return (objectKey, getNumberOfDepartments());
}
