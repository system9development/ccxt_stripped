import { Exchange } from './base/Exchange.js';
export default class deepwaters extends Exchange {
    describe(): any;
    fetchBidsAsks(symbols?: any, params?: {}): Promise<any>;
    fetchTicker(symbol: any, params?: {}): Promise<any>;
    fetchTickers(symbols?: any, params?: {}): Promise<any>;
    fetchMarkets(params?: {}): Promise<void | any[]>;
    fetchCurrencies(params?: {}): Promise<void | {}>;
    fetchOrderBook(symbol: any, limit?: any, params?: {}): Promise<void | import("./base/types.js").OrderBook>;
    fetchBalance(params?: {}): Promise<void | import("./base/types.js").Balances>;
    fetchOrders(symbol?: any, since?: any, limit?: any, params?: {}): Promise<void | import("./base/types.js").Order[]>;
    fetchMyTrades(symbol?: any, since?: any, limit?: any, params?: {}): Promise<void | any[]>;
    fetchOpenOrders(symbol?: any, since?: any, limit?: any, params?: {}): Promise<void | import("./base/types.js").Order[]>;
    fetchClosedOrders(symbol?: any, since?: any, limit?: any, params?: {}): Promise<void | import("./base/types.js").Order[]>;
    fetchCanceledOrders(symbol?: any, since?: any, limit?: any, params?: {}): Promise<void | import("./base/types.js").Order[]>;
    createOrder(symbol: any, type: any, side: any, amount: any, price?: any, params?: {}): Promise<any>;
    fetchOrder(id: any, symbol?: any, params?: {}): Promise<any>;
    cancelOrder(id: any, symbol?: any, params?: {}): Promise<any>;
    cancelAllOrders(symbol?: any, params?: {}): Promise<any>;
    sign(path: any, api?: string, method?: string, params?: {}, headers?: any, body?: any): {
        url: any;
        method: string;
        body: any;
        headers: any;
    };
    loadNonce(): Promise<void>;
    getNonce(): any;
    handleError(response?: {}): void;
    parseOrderStatus(status: any): string;
    parseOrder(order: any, market?: any): any;
    fetchTime(params?: {}): Promise<number | void>;
}
