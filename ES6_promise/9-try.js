export default function guardrail(mathFunction) {
  // array to push values to
  const queue = [];
  const message = 'Guardrail was processed';
  try {
    const value = mathFunction();
    // append value to array
    queue.push(value);
  } catch(error) {
    // push error message
    queue.push('error');
  } finally {
    // in all cases, the message runs
    queue.push(message);
    return queue;
  }
}
