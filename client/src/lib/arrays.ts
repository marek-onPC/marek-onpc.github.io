const switchPlaces = (array: Array<any>, from: number, to: number) => {
  if (array.length < 2) {
    throw new Error('array should have minimum 2 elements');
  }
  if (from < 0 || from > array.length) {
    throw new Error("'from' index is out of scope");
  }
  if (to < 0 || to > array.length) {
    throw new Error("'to' index is out of scope");
  }
  if (from === to) {
    throw new Error("'from' and 'to' are equal");
  }

  const newArray = [...array];

  newArray.splice(to, 0, newArray.splice(from, 1)[0]);

  return newArray;
};

export { switchPlaces };
