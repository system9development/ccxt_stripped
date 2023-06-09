// ----------------------------------------------------------------------------

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code
// EDIT THE CORRESPONDENT .ts FILE INSTEAD

import { inflateRawSync, gunzipSync } from 'zlib';
function inflate(data) {
    return inflateRawSync(data).toString();
}
function inflate64(data) {
    return inflate(Buffer.from(data, 'base64'));
}
function gunzip(data) {
    return gunzipSync(data).toString();
}
export { inflate, inflate64, gunzip, };
