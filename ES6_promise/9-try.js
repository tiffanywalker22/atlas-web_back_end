export default function quardrail(mathFunction) {
  const queue = [];

  try {
    const result = mathFunction();
    queue.push(result);
  } catch (error) {
    queue.push('Error: '.concat(error.message));
  } finally {
    queue.push('Guardrail was processed');
  }

  return queue;
}
