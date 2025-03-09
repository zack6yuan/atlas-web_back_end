export default function handleResponseFromAPI(promise) {
  return new Promise((resolve, reject) => {
    if (promise(resolve) == true) {
     return {
      status: 200,
      body: 'success',
     };
     console.log('got a response from the API')
    } else {
      reject(new Error(''))
      const errorObject = [];

      return errorObject;
    };
  })
}
