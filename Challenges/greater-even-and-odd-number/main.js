const mainFunction = (input) => {
  if (typeof input !== 'string') throw 'Invalid input';
  const allDigits = input.split('').map(Number);
  const posibleNumbers = [];
  allDigits.forEach((digit, index, arr) => {
    if (arr.length - 2 < index) return;
    posibleNumbers.push(Number(`${digit}${arr[index + 1]}`));
  });
  const maxEvenNumber = Math.max(
    ...posibleNumbers.filter((num) => num % 2 === 0)
  );
  const maxOddNumber = Math.max(
    ...posibleNumbers.filter((num) => num % 2 !== 0)
  );
  return [maxEvenNumber, maxOddNumber];
};

console.log(mainFunction('726437856347856837657834'));
