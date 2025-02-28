export default function returnHowManyArguments(...args) {
  total = 0;
  for (let arg of args) total += arg;
  return total;
}