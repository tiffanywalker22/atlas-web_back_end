export default function updateUniqueItems(groceries) {
  if (!(groceries instanceof Map)) {
    throw new Error('Cannot process');
  }
  const newGroceries = new Map();

  groceries.forEach((quanity, item) => {
    if (quanity === 1) {
      newGroceries.set(item, 100);
    } else {
      newGroceries.set(item, quanity);
    }
  });
  return newGroceries;
}
