export default function loadBalancer(chinaDownload, USDownload) {
  const myPromise = new Promise((resolve, reject) => {
    if (chinaDownload && USDownload) {
      resolve(myPromise);
    } else {
      reject(new Error('error'))
    }
  })
}
