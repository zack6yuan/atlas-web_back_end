export default function signUpUser(firstName, lastName) {
  return new Promise((resolve, reject) => {
    if (firstName && lastName) {
      const names = {
        firstName: firstName,
        lastName: lastName,
      };
      resolve(names);
    } else {
      reject(new Error('firstName and lastName are not valid.'));
    }
  });
}
