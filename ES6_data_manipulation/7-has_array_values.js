export default function hasValuesFromArray(set, array) {
  if (array instanceof set) {
    return true;
  } else {
    return false;
  }
}
