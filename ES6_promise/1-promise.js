getFullResponseFromAPI(success); {
  return new Promise((resolve, reject) => {
    if (success) {
      const object = {
        status: 200,
        body: 'Success',
      };
      resolve(object);
    } else {
      reject(new Error('The fake API is not working currently'));
    }
  });
}
