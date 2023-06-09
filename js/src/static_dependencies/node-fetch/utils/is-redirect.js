// ----------------------------------------------------------------------------

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code
// EDIT THE CORRESPONDENT .ts FILE INSTEAD

const redirectStatus = new Set([301, 302, 303, 307, 308]);
/**
 * Redirect code matching
 *
 * @param {number} code - Status code
 * @return {boolean}
 */
export const isRedirect = code => {
    return redirectStatus.has(code);
};
