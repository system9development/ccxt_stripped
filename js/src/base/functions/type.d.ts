declare const isNumber: (number: unknown) => boolean;
declare const isInteger: (number: unknown) => boolean;
declare const isArray: (arg: any) => arg is any[];
declare const hasProps: (o: any) => boolean;
declare const isString: (s: any) => boolean;
declare const isObject: (o: any) => boolean;
declare const isDictionary: (o: any) => boolean;
declare const isStringCoercible: (x: any) => any;
declare const prop: (o: any, k: any) => any;
declare const asFloat: (x: any) => number;
declare const asInteger: (x: any) => number;
declare const safeFloat: (o: object, k: string | number, $default?: number) => number;
declare const safeInteger: (o: object, k: string | number, $default?: number) => number;
declare const safeIntegerProduct: (o: object, k: string | number, $factor: number, $default?: number) => number;
declare const safeTimestamp: (o: object, k: string | number, $default?: number) => number;
declare const safeValue: (o: object, k: string | number, $default?: any) => any;
declare const safeString: (o: object, k: string | number, $default?: string) => string;
declare const safeStringLower: (o: object, k: string | number, $default?: string) => string;
declare const safeStringUpper: (o: object, k: string | number, $default?: string) => string;
declare const safeFloat2: (o: object, k1: string | number, k2: string | number, $default?: number) => number;
declare const safeInteger2: (o: object, k1: string | number, k2: string | number, $default?: number) => number;
declare const safeIntegerProduct2: (o: object, k1: string | number, k2: string | number, $factor: number, $default?: number) => number;
declare const safeTimestamp2: (o: object, k1: string | number, k2: string | number, $default?: any) => number;
declare const safeValue2: (o: object, k1: string | number, k2: string | number, $default?: any) => any;
declare const safeString2: (o: object, k1: string | number, k2: string | number, $default?: string) => string;
declare const safeStringLower2: (o: object, k1: string | number, k2: string | number, $default?: string) => string;
declare const safeStringUpper2: (o: object, k1: string | number, k2: string | number, $default?: string) => string;
declare const safeFloatN: (o: object, k: (string | number)[], $default?: number) => number;
declare const safeIntegerN: (o: object, k: (string | number)[], $default?: number) => number;
declare const safeIntegerProductN: (o: object, k: (string | number)[], $factor: number, $default?: number) => number;
declare const safeTimestampN: (o: object, k: (string | number)[], $default?: number) => number;
declare const safeValueN: (o: object, k: (string | number)[], $default?: any) => any;
declare const safeStringN: (o: object, k: (string | number)[], $default?: string) => string;
declare const safeStringLowerN: (o: object, k: (string | number)[], $default?: string) => string;
declare const safeStringUpperN: (o: object, k: (string | number)[], $default?: string) => string;
export { isNumber, isInteger, isArray, isObject, isString, isStringCoercible, isDictionary, hasProps, prop, asFloat, asInteger, safeFloat, safeInteger, safeIntegerProduct, safeTimestamp, safeValue, safeString, safeStringLower, safeStringUpper, safeFloat2, safeInteger2, safeIntegerProduct2, safeTimestamp2, safeValue2, safeString2, safeStringLower2, safeStringUpper2, safeFloatN, safeIntegerN, safeIntegerProductN, safeTimestampN, safeValueN, safeStringN, safeStringLowerN, safeStringUpperN, };
