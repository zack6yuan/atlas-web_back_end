export default function guardrail(mathFunction) {
  // array to push values to
  const queue = [];
  const message = 'Guardrail was processed';
  try {
    const value = mathFunction();
    // append value to array
    queue.push(value, message);
  } catch(error) {
    // push error message
    queue.push('Error', message);
  } finally {
    return queue;
  }
}
