import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const myPromise = new Promise((resolve, reject) => {
    if (firstName && lastName && fileName) {
      signUpUser()
      uploadPhoto()
    }
    resolve(myPromise);
    const array = {
      status: 
      value:
    }
    return array;
  })
}

// work in progress