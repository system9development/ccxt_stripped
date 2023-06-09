<?php
namespace ccxt;

// ----------------------------------------------------------------------------

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

// -----------------------------------------------------------------------------

function test_leverage_tier($exchange, $method, $tier) {
    $format = array(
        'tier' => 1,
        'minNotional' => 0,
        'maxNotional' => 5000,
        'maintenanceMarginRate' => 0.01,
        'maxLeverage' => 25,
        'info' => array(),
    );
    $keys = is_array($format) ? array_keys($format) : array();
    for ($i = 0; $i < count($keys); $i++) {
        $key = $keys[$i];
    }
    if ($tier['tier'] !== null) {
        assert ((is_float($tier['tier']) || is_int($tier['tier'])));
        assert ($tier['tier'] >= 0);
    }
    if ($tier['minNotional'] !== null) {
        assert ((is_float($tier['minNotional']) || is_int($tier['minNotional'])));
        assert ($tier['minNotional'] >= 0);
    }
    if ($tier['maxNotional'] !== null) {
        assert ((is_float($tier['maxNotional']) || is_int($tier['maxNotional'])));
        assert ($tier['maxNotional'] >= 0);
    }
    if ($tier['maxLeverage'] !== null) {
        assert ((is_float($tier['maxLeverage']) || is_int($tier['maxLeverage'])));
        assert ($tier['maxLeverage'] >= 1);
    }
    if ($tier['maintenanceMarginRate'] !== null) {
        assert ((is_float($tier['maintenanceMarginRate']) || is_int($tier['maintenanceMarginRate'])));
        assert ($tier['maintenanceMarginRate'] <= 1);
    }
    var_dump ($exchange->id, $method, $tier['tier'], $tier['minNotional'], $tier['maxNotional'], $tier['maintenanceMarginRate'], $tier['maxLeverage']);
    return $tier;
}

