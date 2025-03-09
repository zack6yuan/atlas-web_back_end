export default function handleResponseFromAPI(promise) {
  return new Promise((resolve, reject) => {
    if (promise) {
      const object = {
        status: 200,
        body: 'success',
      }
      resolve(object);
    } else {
      reject(new Error);
    };
  })
}
