const sm2 = require('sm-crypto').sm2;

let publicKey = "042ee9d52a0d31f1e4f9f16a636154179ed3386706add6439b778e7cc7792743b1a75076fb9682411a87ecef88652999f646a0a9b232ceecde59b5c39e7bb49f2f"
let msg = "action=listCMInfo&pubKey=" + publicKey;
let privateKey = "ab8c753378a031976cf2a848e57299240cdbbdecf36e726aa8a1e4a9fa9046e1";
let sigValueHex = sm2.doSignature(msg, privateKey);
console.log(sigValueHex)
let verifyResult = sm2.doVerifySignature(msg, sigValueHex, publicKey);
console.log(verifyResult)
