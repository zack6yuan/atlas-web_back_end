export default function loadBalancer(chinaDownload, USDownload) {
  // promise.any => return the promise that resolves first
 return  Promise.any([chinaDownload, USDownload])
}
