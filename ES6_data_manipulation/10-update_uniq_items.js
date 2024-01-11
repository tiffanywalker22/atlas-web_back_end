export default function updateUniqueItems(groceries) {
  if (!(groceries instanceof Map)) {
    throw new Error('Cannot process');
  }

  for (const [quanity, item] of groceries) {
    if (quanity === 1) {
      groceries.set(item, 100);
    }
  }
  return groceries;
}
