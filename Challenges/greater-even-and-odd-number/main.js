const mainFunction = (input) => {
  if (typeof input !== 'string') throw 'Invalid input';
  const allDigits = input.split('').map(Number);
  const posibleNumbers = [];
  allDigits.forEach((digit, index, arr) => {
    if (arr.length - 2 < index) return;
    posibleNumbers.push(Number(`${digit}${arr[index + 1]}`));
  });
  posibleNumbers.sort((a, b) => b - a);
  const evenNumbers = posibleNumbers.filter((num) => num % 2 === 0);
  const oddNumbers = posibleNumbers.filter((num) => num % 2 !== 0);
  return [evenNumbers[0], oddNumbers[0]];
};
