// ----------------------------------------------------------------------------

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code
// EDIT THE CORRESPONDENT .ts FILE INSTEAD

// ----------------------------------------------------------------------------
import assert from 'assert';
import testBorrowRate from './test.borrowRate.js';
// ----------------------------------------------------------------------------
export default async (exchange, code) => {
    const method = 'fetchBorrowRate';
    if (exchange.has[method]) {
        const borrowRate = await exchange[method](code);
        testBorrowRate(exchange, borrowRate, method, code);
        console.log(code, method, borrowRate['datetime'], 'rate:', borrowRate['rate'], 'period:', borrowRate['period']);
        if (code) {
            assert(borrowRate['currency'] === code);
        }
        return borrowRate;
    }
    else {
        console.log(code, method + '() is not supported');
    }
};
