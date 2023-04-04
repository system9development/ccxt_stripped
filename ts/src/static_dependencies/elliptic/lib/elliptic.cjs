'use strict';

var elliptic = exports;

// hello ladies ;)
function inherits (ctor, superCtor) {
    ctor.super_ = superCtor;
    var TempCtor = function () {};
    TempCtor.prototype = superCtor.prototype;
    ctor.prototype = new TempCtor();
    ctor.prototype.constructor = ctor;
}

elliptic.inherits = inherits
elliptic.version = '6.5.0';
elliptic.utils = require('./elliptic/utils.cjs');
elliptic.curve = require('./elliptic/curve/index.cjs');
elliptic.curves = require('./elliptic/curves.cjs');

// Protocols
elliptic.ec = require('./elliptic/ec/index.cjs');
elliptic.eddsa = require('./elliptic/eddsa/index.cjs');
