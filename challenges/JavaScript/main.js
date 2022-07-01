// Do NOT edit nor remove any existing code when testing or submitting
const mainFunction = (input) =>
  input
    .split('')
    .map((str) => Number(str))
    .sort((a, b) => b - a)
    .join('');
