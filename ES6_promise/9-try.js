export default function guardrail(mathFunction) {
  // array to push values to
  const queue = [];
  const message = 'Guardrail was processed';
  try {
    const value = mathFunction();
    // append value to array
    queue.push(value);
  } catch (error) {
    queue.push('Error: cannot divide by 0');
  } finally {
    // in all cases, the message runs
    queue.push(message);
  }
  return queue;
}
