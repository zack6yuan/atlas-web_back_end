export default function guardrail(mathFunction) {
  const queue = [];
  .try(mathFunction())
  .then(() => {
    queue.push()
  })

  // When the mathFunction function is executed, the value 
  // returned by the function should be appended to the queue. 
  // If this function throws an error, the error message should 
  // be appended to the queue. In every case, the message Guardrail 
  // was processed should be added to the queue.
