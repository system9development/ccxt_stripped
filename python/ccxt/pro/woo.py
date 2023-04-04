# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

import ccxt.async_support
from ccxt.async_support.base.ws.cache import ArrayCache, ArrayCacheBySymbolById, ArrayCacheByTimestamp
import hashlib
from ccxt.base.errors import ExchangeError
from ccxt.base.errors import AuthenticationError
from ccxt.base.precise import Precise


class woo(ccxt.async_support.woo):

    def describe(self):
        return self.deep_extend(super(woo, self).describe(), {
            'has': {
                'ws': True,
                'watchBalance': False,
                'watchMyTrades': False,
                'watchOHLCV': True,
                'watchOrderBook': True,
                'watchOrders': True,
                'watchTicker': True,
                'watchTickers': True,
                'watchTrades': True,
            },
            'urls': {
                'api': {
                    'ws': {
                        'public': 'wss://wss.woo.org/ws/stream',
                        'private': 'wss://wss.woo.network/v2/ws/private/stream',
                    },
                },
                'test': {
                    'ws': {
                        'public': 'wss://wss.staging.woo.org/ws/stream',
                        'private': 'wss://wss.staging.woo.org/v2/ws/private/stream',
                    },
                },
            },
            'requiredCredentials': {
                'apiKey': True,
                'secret': True,
                'uid': True,
            },
            'options': {
                'tradesLimit': 1000,
                'ordersLimit': 1000,
                'requestId': {},
            },
            'streaming': {
                'ping': self.ping,
                'keepAlive': 10000,
            },
        })

    def request_id(self, url):
        options = self.safe_value(self.options, 'requestId', {})
        previousValue = self.safe_integer(options, url, 0)
        newValue = self.sum(previousValue, 1)
        self.options['requestId'][url] = newValue
        return newValue

    async def watch_public(self, messageHash, message):
        self.check_required_uid()
        url = self.urls['api']['ws']['public'] + '/' + self.uid
        requestId = self.request_id(url)
        subscribe = {
            'id': requestId,
        }
        request = self.extend(subscribe, message)
        return await self.watch(url, messageHash, request, messageHash, subscribe)

    async def watch_order_book(self, symbol, limit=None, params={}):
        await self.load_markets()
        name = 'orderbook'
        market = self.market(symbol)
        topic = market['id'] + '@' + name
        request = {
            'event': 'subscribe',
            'topic': topic,
        }
        message = self.extend(request, params)
        orderbook = await self.watch_public(topic, message)
        return orderbook.limit()

    def handle_order_book(self, client, message):
        #
        #     {
        #         topic: 'PERP_BTC_USDT@orderbook',
        #         ts: 1650121915308,
        #         data: {
        #             symbol: 'PERP_BTC_USDT',
        #             bids: [
        #                 [
        #                     0.30891,
        #                     2469.98
        #                 ]
        #             ],
        #             asks: [
        #                 [
        #                     0.31075,
        #                     2379.63
        #                 ]
        #             ]
        #         }
        #     }
        #
        data = self.safe_value(message, 'data')
        marketId = self.safe_string(data, 'symbol')
        market = self.safe_market(marketId)
        symbol = market['symbol']
        topic = self.safe_string(message, 'topic')
        orderbook = self.safe_value(self.orderbooks, symbol)
        if orderbook is None:
            orderbook = self.order_book({})
        timestamp = self.safe_integer(message, 'ts')
        snapshot = self.parse_order_book(data, symbol, timestamp, 'bids', 'asks')
        orderbook.reset(snapshot)
        client.resolve(orderbook, topic)

    async def watch_ticker(self, symbol, params={}):
        await self.load_markets()
        name = 'ticker'
        market = self.market(symbol)
        topic = market['id'] + '@' + name
        request = {
            'event': 'subscribe',
            'topic': topic,
        }
        message = self.extend(request, params)
        return await self.watch_public(topic, message)

    def parse_ws_ticker(self, ticker, market=None):
        #
        #     {
        #         symbol: 'PERP_BTC_USDT',
        #         open: 19441.5,
        #         close: 20147.07,
        #         high: 20761.87,
        #         low: 19320.54,
        #         volume: 2481.103,
        #         amount: 50037935.0286,
        #         count: 3689
        #     }
        #
        timestamp = self.safe_integer(ticker, 'date', self.milliseconds())
        return self.safe_ticker({
            'symbol': self.safe_symbol(None, market),
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'high': self.safe_string(ticker, 'high'),
            'low': self.safe_string(ticker, 'low'),
            'bid': None,
            'bidVolume': None,
            'ask': None,
            'askVolume': None,
            'vwap': None,
            'open': self.safe_string(ticker, 'open'),
            'close': self.safe_string(ticker, 'close'),
            'last': None,
            'previousClose': None,
            'change': None,
            'percentage': None,
            'average': None,
            'baseVolume': self.safe_string(ticker, 'volume'),
            'quoteVolume': self.safe_string(ticker, 'amount'),
            'info': ticker,
        }, market)

    def handle_ticker(self, client, message):
        #
        #     {
        #         topic: 'PERP_BTC_USDT@ticker',
        #         ts: 1657120017000,
        #         data: {
        #             symbol: 'PERP_BTC_USDT',
        #             open: 19441.5,
        #             close: 20147.07,
        #             high: 20761.87,
        #             low: 19320.54,
        #             volume: 2481.103,
        #             amount: 50037935.0286,
        #             count: 3689
        #         }
        #     }
        #
        data = self.safe_value(message, 'data')
        topic = self.safe_value(message, 'topic')
        marketId = self.safe_string(data, 'symbol')
        market = self.safe_market(marketId)
        timestamp = self.safe_integer(message, 'ts')
        data['date'] = timestamp
        ticker = self.parse_ws_ticker(data, market)
        ticker['symbol'] = market['symbol']
        self.tickers[market['symbol']] = ticker
        client.resolve(ticker, topic)
        return message

    async def watch_tickers(self, symbols=None, params={}):
        await self.load_markets()
        name = 'tickers'
        topic = name
        request = {
            'event': 'subscribe',
            'topic': topic,
        }
        message = self.extend(request, params)
        tickers = await self.watch_public(topic, message)
        return self.filter_by_array(tickers, 'symbol', symbols)

    def handle_tickers(self, client, message):
        #
        #     {
        #         "topic":"tickers",
        #         "ts":1618820615000,
        #         "data":[
        #             {
        #                 "symbol":"SPOT_OKB_USDT",
        #                 "open":16.297,
        #                 "close":17.183,
        #                 "high":24.707,
        #                 "low":11.997,
        #                 "volume":0,
        #                 "amount":0,
        #                 "count":0
        #             },
        #             {
        #                 "symbol":"SPOT_XRP_USDT",
        #                 "open":1.3515,
        #                 "close":1.43794,
        #                 "high":1.96674,
        #                 "low":0.39264,
        #                 "volume":750127.1,
        #                 "amount":985440.5122,
        #                 "count":396
        #             },
        #         ...
        #         ]
        #     }
        #
        topic = self.safe_value(message, 'topic')
        data = self.safe_value(message, 'data')
        timestamp = self.safe_integer(message, 'ts')
        result = []
        for i in range(0, len(data)):
            marketId = self.safe_string(data[i], 'symbol')
            market = self.safe_market(marketId)
            ticker = self.parse_ws_ticker(self.extend(data[i], {'date': timestamp}), market)
            self.tickers[market['symbol']] = ticker
            result.append(ticker)
        client.resolve(result, topic)

    async def watch_ohlcv(self, symbol, timeframe='1m', since=None, limit=None, params={}):
        await self.load_markets()
        if (timeframe != '1m') and (timeframe != '5m') and (timeframe != '15m') and (timeframe != '30m') and (timeframe != '1h') and (timeframe != '1d') and (timeframe != '1w') and (timeframe != '1M'):
            raise ExchangeError(self.id + ' watchOHLCV timeframe argument must be 1m, 5m, 15m, 30m, 1h, 1d, 1w, 1M')
        market = self.market(symbol)
        interval = self.safe_string(self.timeframes, timeframe, timeframe)
        name = 'kline'
        topic = market['id'] + '@' + name + '_' + interval
        request = {
            'event': 'subscribe',
            'topic': topic,
        }
        message = self.extend(request, params)
        ohlcv = await self.watch_public(topic, message)
        if self.newUpdates:
            limit = ohlcv.getLimit(market['symbol'], limit)
        return self.filter_by_since_limit(ohlcv, since, limit, 0, True)

    def handle_ohlcv(self, client, message):
        #
        #     {
        #         "topic":"SPOT_BTC_USDT@kline_1m",
        #         "ts":1618822432146,
        #         "data":{
        #             "symbol":"SPOT_BTC_USDT",
        #             "type":"1m",
        #             "open":56948.97,
        #             "close":56891.76,
        #             "high":56948.97,
        #             "low":56889.06,
        #             "volume":44.00947568,
        #             "amount":2504584.9,
        #             "startTime":1618822380000,
        #             "endTime":1618822440000
        #         }
        #     }
        #
        data = self.safe_value(message, 'data')
        topic = self.safe_value(message, 'topic')
        marketId = self.safe_string(data, 'symbol')
        market = self.safe_market(marketId)
        symbol = market['symbol']
        interval = self.safe_string(data, 'type')
        timeframe = self.find_timeframe(interval)
        parsed = [
            self.safe_integer(data, 'startTime'),
            self.safe_float(data, 'open'),
            self.safe_float(data, 'high'),
            self.safe_float(data, 'low'),
            self.safe_float(data, 'close'),
            self.safe_float(data, 'volume'),
        ]
        self.ohlcvs[symbol] = self.safe_value(self.ohlcvs, symbol, {})
        stored = self.safe_value(self.ohlcvs[symbol], timeframe)
        if stored is None:
            limit = self.safe_integer(self.options, 'OHLCVLimit', 1000)
            stored = ArrayCacheByTimestamp(limit)
            self.ohlcvs[symbol][timeframe] = stored
        stored.append(parsed)
        client.resolve(stored, topic)

    async def watch_trades(self, symbol, since=None, limit=None, params={}):
        await self.load_markets()
        market = self.market(symbol)
        topic = market['id'] + '@trade'
        request = {
            'event': 'subscribe',
            'topic': topic,
        }
        message = self.extend(request, params)
        trades = await self.watch_public(topic, message)
        if self.newUpdates:
            limit = trades.getLimit(market['symbol'], limit)
        return self.filter_by_symbol_since_limit(trades, symbol, since, limit, True)

    def handle_trade(self, client, message):
        #
        # {
        #     "topic":"SPOT_ADA_USDT@trade",
        #     "ts":1618820361552,
        #     "data":{
        #         "symbol":"SPOT_ADA_USDT",
        #         "price":1.27988,
        #         "size":300,
        #         "side":"BUY",
        #         "source":0
        #     }
        # }
        #
        topic = self.safe_string(message, 'topic')
        timestamp = self.safe_integer(message, 'ts')
        data = self.safe_value(message, 'data')
        marketId = self.safe_string(data, 'symbol')
        market = self.safe_market(marketId)
        symbol = market['symbol']
        trade = self.parse_ws_trade(self.extend(data, {'timestamp': timestamp}), market)
        tradesArray = self.safe_value(self.trades, symbol)
        if tradesArray is None:
            limit = self.safe_integer(self.options, 'tradesLimit', 1000)
            tradesArray = ArrayCache(limit)
        tradesArray.append(trade)
        self.trades[symbol] = tradesArray
        client.resolve(tradesArray, topic)

    def parse_ws_trade(self, trade, market=None):
        #
        #     {
        #         "symbol":"SPOT_ADA_USDT",
        #         "timestamp":1618820361552,
        #         "price":1.27988,
        #         "size":300,
        #         "side":"BUY",
        #         "source":0
        #     }
        #
        marketId = self.safe_string(trade, 'symbol')
        market = self.safe_market(marketId, market)
        symbol = market['symbol']
        price = self.safe_string(trade, 'price')
        amount = self.safe_string(trade, 'size')
        cost = Precise.string_mul(price, amount)
        side = self.safe_string_lower(trade, 'side')
        timestamp = self.safe_integer(trade, 'timestamp')
        return self.safe_trade({
            'id': None,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': symbol,
            'side': side,
            'price': price,
            'amount': amount,
            'cost': cost,
            'order': None,
            'takerOrMaker': None,
            'type': None,
            'fee': None,
            'info': trade,
        }, market)

    def check_required_uid(self, error=True):
        if not self.uid:
            if error:
                raise AuthenticationError(self.id + ' requires `uid` credential')
            else:
                return False
        return True

    def authenticate(self, params={}):
        self.check_required_credentials()
        url = self.urls['api']['ws']['private'] + '/' + self.uid
        client = self.client(url)
        messageHash = 'authenticated'
        event = 'auth'
        future = self.safe_value(client.subscriptions, messageHash)
        if future is None:
            ts = str(self.nonce())
            auth = '|' + ts
            signature = self.hmac(self.encode(auth), self.encode(self.secret), hashlib.sha256)
            request = {
                'event': event,
                'params': {
                    'apikey': self.apiKey,
                    'sign': signature,
                    'timestamp': ts,
                },
            }
            message = self.extend(request, params)
            future = self.watch(url, messageHash, message)
            client.subscriptions[messageHash] = future
        return future

    async def watch_private(self, messageHash, message, params={}):
        await self.authenticate(params)
        url = self.urls['api']['ws']['private'] + '/' + self.uid
        requestId = self.request_id(url)
        subscribe = {
            'id': requestId,
        }
        request = self.extend(subscribe, message)
        return await self.watch(url, messageHash, request, messageHash, subscribe)

    async def watch_orders(self, symbol=None, since=None, limit=None, params={}):
        await self.load_markets()
        topic = 'executionreport'
        messageHash = topic
        if symbol is not None:
            market = self.market(symbol)
            symbol = market['symbol']
            messageHash += ':' + symbol
        request = {
            'event': 'subscribe',
            'topic': topic,
        }
        message = self.extend(request, params)
        orders = await self.watch_private(messageHash, message)
        if self.newUpdates:
            limit = orders.getLimit(symbol, limit)
        return self.filter_by_symbol_since_limit(orders, symbol, since, limit, True)

    def parse_ws_order(self, order, market=None):
        #
        #     {
        #         symbol: 'PERP_BTC_USDT',
        #         clientOrderId: 0,
        #         orderId: 52952826,
        #         type: 'LIMIT',
        #         side: 'SELL',
        #         quantity: 0.01,
        #         price: 22000,
        #         tradeId: 0,
        #         executedPrice: 0,
        #         executedQuantity: 0,
        #         fee: 0,
        #         feeAsset: 'USDT',
        #         totalExecutedQuantity: 0,
        #         status: 'NEW',
        #         reason: '',
        #         orderTag: 'default',
        #         totalFee: 0,
        #         visible: 0.01,
        #         timestamp: 1657515556799,
        #         reduceOnly: False,
        #         maker: False
        #     }
        #
        orderId = self.safe_string(order, 'orderId')
        marketId = self.safe_string(order, 'symbol')
        market = self.market(marketId)
        symbol = market['symbol']
        timestamp = self.safe_integer(order, 'timestamp')
        cost = self.safe_string(order, 'totalFee')
        fee = {
            'cost': cost,
            'currency': self.safe_string(order, 'feeAsset'),
        }
        price = self.safe_float(order, 'price')
        amount = self.safe_float(order, 'quantity')
        side = self.safe_string_lower(order, 'side')
        type = self.safe_string_lower(order, 'type')
        filled = self.safe_float(order, 'executedQuantity')
        totalExecQuantity = self.safe_float(order, 'totalExecutedQuantity')
        remaining = amount
        if amount >= totalExecQuantity:
            remaining -= totalExecQuantity
        rawStatus = self.safe_string(order, 'status')
        status = self.parse_order_status(rawStatus)
        trades = None
        clientOrderId = self.safe_string(order, 'clientOrderId')
        return {
            'info': order,
            'symbol': symbol,
            'id': orderId,
            'clientOrderId': clientOrderId,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'lastTradeTimestamp': timestamp,
            'type': type,
            'timeInForce': None,
            'postOnly': None,
            'side': side,
            'price': price,
            'stopPrice': None,
            'triggerPrice': None,
            'amount': amount,
            'cost': cost,
            'average': None,
            'filled': filled,
            'remaining': remaining,
            'status': status,
            'fee': fee,
            'trades': trades,
        }

    def handle_order_update(self, client, message):
        #
        #     {
        #         topic: 'executionreport',
        #         ts: 1657515556799,
        #         data: {
        #             symbol: 'PERP_BTC_USDT',
        #             clientOrderId: 0,
        #             orderId: 52952826,
        #             type: 'LIMIT',
        #             side: 'SELL',
        #             quantity: 0.01,
        #             price: 22000,
        #             tradeId: 0,
        #             executedPrice: 0,
        #             executedQuantity: 0,
        #             fee: 0,
        #             feeAsset: 'USDT',
        #             totalExecutedQuantity: 0,
        #             status: 'NEW',
        #             reason: '',
        #             orderTag: 'default',
        #             totalFee: 0,
        #             visible: 0.01,
        #             timestamp: 1657515556799,
        #             reduceOnly: False,
        #             maker: False
        #         }
        #     }
        #
        order = self.safe_value(message, 'data')
        self.handle_order(client, order)

    def handle_order(self, client, message):
        topic = 'executionreport'
        parsed = self.parse_ws_order(message)
        symbol = self.safe_string(parsed, 'symbol')
        orderId = self.safe_string(parsed, 'id')
        if symbol is not None:
            if self.orders is None:
                limit = self.safe_integer(self.options, 'ordersLimit', 1000)
                self.orders = ArrayCacheBySymbolById(limit)
            cachedOrders = self.orders
            orders = self.safe_value(cachedOrders.hashmap, symbol, {})
            order = self.safe_value(orders, orderId)
            if order is not None:
                fee = self.safe_value(order, 'fee')
                if fee is not None:
                    parsed['fee'] = fee
                fees = self.safe_value(order, 'fees')
                if fees is not None:
                    parsed['fees'] = fees
                parsed['trades'] = self.safe_value(order, 'trades')
                parsed['timestamp'] = self.safe_integer(order, 'timestamp')
                parsed['datetime'] = self.safe_string(order, 'datetime')
            cachedOrders.append(parsed)
            client.resolve(self.orders, topic)
            messageHashSymbol = topic + ':' + symbol
            client.resolve(self.orders, messageHashSymbol)

    def handle_message(self, client, message):
        methods = {
            'ping': self.handle_ping,
            'pong': self.handle_pong,
            'subscribe': self.handle_subscribe,
            'orderbook': self.handle_order_book,
            'ticker': self.handle_ticker,
            'tickers': self.handle_tickers,
            'kline': self.handle_ohlcv,
            'auth': self.handle_auth,
            'executionreport': self.handle_order_update,
            'trade': self.handle_trade,
        }
        event = self.safe_string(message, 'event')
        method = self.safe_value(methods, event)
        if method is not None:
            return method(client, message)
        topic = self.safe_string(message, 'topic')
        if topic is not None:
            method = self.safe_value(methods, topic)
            if method is not None:
                return method(client, message)
            splitTopic = topic.split('@')
            splitLength = len(splitTopic)
            if splitLength == 2:
                name = self.safe_string(splitTopic, 1)
                method = self.safe_value(methods, name)
                if method is not None:
                    return method(client, message)
                splitName = name.split('_')
                splitNameLength = len(splitTopic)
                if splitNameLength == 2:
                    method = self.safe_value(methods, self.safe_string(splitName, 0))
                    if method is not None:
                        return method(client, message)
        return message

    def ping(self, client):
        return {'event': 'ping'}

    def handle_ping(self, client, message):
        return {'event': 'pong'}

    def handle_pong(self, client, message):
        #
        # {event: 'pong', ts: 1657117026090}
        #
        client.lastPong = self.milliseconds()
        return message

    def handle_subscribe(self, client, message):
        #
        #     {
        #         id: '666888',
        #         event: 'subscribe',
        #         success: True,
        #         ts: 1657117712212
        #     }
        #
        return message

    def handle_auth(self, client, message):
        #
        #     {
        #         event: 'auth',
        #         success: True,
        #         ts: 1657463158812
        #     }
        #
        messageHash = 'authenticated'
        success = self.safe_value(message, 'success')
        if success:
            client.resolve(message, messageHash)
        else:
            error = AuthenticationError(self.json(message))
            client.reject(error, messageHash)
            # allows further authentication attempts
            if messageHash in client.subscriptions:
                del client.subscriptions['authenticated']
