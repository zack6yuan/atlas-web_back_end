export default function uploadPhoto(filename) {
  return new Promise((resolve, reject) => {
    if (filename) {
      resolve()
    } else {
      reject(new Error(`${filename} cannot be processed`));
    }
  });
}
