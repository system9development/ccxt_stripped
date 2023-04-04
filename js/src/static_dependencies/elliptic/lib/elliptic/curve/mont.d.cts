// ----------------------------------------------------------------------------

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code
// EDIT THE CORRESPONDENT .ts FILE INSTEAD

export = MontCurve;
declare function MontCurve(conf: any): void;
declare class MontCurve {
    constructor(conf: any);
    a: any;
    b: any;
    i4: any;
    two: any;
    a24: any;
    validate(point: any): boolean;
    decodePoint(bytes: any, enc: any): Point;
    point(x: any, z: any): Point;
    pointFromJSON(obj: any): Point;
}
declare function Point(curve: any, x: any, z: any): void;
declare class Point {
    constructor(curve: any, x: any, z: any);
    x: any;
    z: any;
    precompute(): void;
    _encode(): any;
    inspect(): string;
    isInfinity(): boolean;
    dbl(): any;
    add(): never;
    diffAdd(p: any, diff: any): any;
    mul(k: any): any;
    mulAdd(): never;
    jumlAdd(): never;
    eq(other: any): boolean;
    normalize(): Point;
    getX(): any;
}
declare namespace Point {
    function fromJSON(curve: any, obj: any): Point;
}
