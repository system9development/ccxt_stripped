// ----------------------------------------------------------------------------

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code
// EDIT THE CORRESPONDENT .ts FILE INSTEAD

export = Signature;
declare function Signature(options: any, enc: any): Signature;
declare class Signature {
    constructor(options: any, enc: any);
    r: BN;
    s: BN;
    recoveryParam: any;
}
import BN = require("../../../../BN/bn.cjs");
