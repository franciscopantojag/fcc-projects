/**
 * @param {number} input
 * @return {number}
 */

const findProductDigits = (input) => {
  const str = input.toString();
  const arr = str.split('').reduce((acc, digit) => acc * digit);
  return arr;
};

/**
 * @param {number} input
 */

const mainFunction = (input) => {
  let result = findProductDigits(input);
  let resultLength = result.toString().length;
  while (resultLength >= 2) {
    result = findProductDigits(result);
    resultLength = result.toString().length;
  }
  return result;
};

console.log(mainFunction('72'));
