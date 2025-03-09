export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => { // success
      const object = {
        status: '200',
        body: 'success',
      }
      return object;
    })
    .catch((error) => error) // empty error object
    .finally(() => console.log('Got a response from the API'));
  };
