const mainFunction = (input) =>
  input
    .split('')
    .map((str) => Number(str))
    .sort((a, b) => b - a)
    .join('');
