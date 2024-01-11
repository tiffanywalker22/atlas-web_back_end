export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string') {
    return '';
  }
  const filterValues = Array.from(set).filter((value) => value.startsWith(startString))
    .map((value) => value.replace(startString, ''));

  const endString = filterValues.join('-');
  return endString;
}
