export default function loadBalancer(chinaDownload, USDownload) {
  // promise.any => return the promise that resolves first
  Promise.any(chinaDownload, USDownload)
}
