from enum import Enum


# API paths
class Path(object):
    # Public
    SERVER_TIME = 'public/Time'
    ASSETS = 'public/Assets'
    ASSET_PAIRS = 'public/AssetPairs'
    TICKER = 'public/Ticker'
    OHCL = 'public/OHCL'
    ORDER_BOOK = 'public/Depth'
    TRADES = 'public/Trades'
    SPREAD = 'public/Spread'
    # Private user data
    BALANCE = 'private/Balance'
    TRADE_BALANCE = 'private/TradeBalance'
    OPEN_ORDERS = 'private/OpenOrders'
    CLOSED_ORDERS = 'private/ClosedOrders'
    QUERY_ORDERS = 'private/QueryOrders'
    TRADES_HISTORY = 'private/TradesHistory'
    QUERY_TRADES = 'private/QueryTrades'
    OPEN_POSITIONS = 'private/OpenPositions'
    LEDGERS = 'private/Ledgers'
    QUERY_LEDGERS = 'private/QueryLedgers'
    TRADE_VOLUME = 'private/TradeVolume'
    # Private user trading
    ADD_ORDER = 'private/AddOrder'
    CANCEL_ORDER = 'private/CancelOrder'
    # Private user funding
    DEPOSIT_METHODS = 'private/DepositMethods'
    DEPOSIT_ADDRESSES = 'private/DepositAddresses'
    DEPOSIT_STATUS = 'private/DepositStatus'
    WITHDRAW_INFO = 'private/WithdrawInfo'
    WITHDRAW = 'private/Withdraw'
    WITHDRAW_STATUS = 'private/WithdrawStatus'
    WITHDRAW_CANCEL = 'private/WithdrawCancel'


class _Enum(Enum):

    @staticmethod
    def _format_value(value):
        return str(value).upper()

    @classmethod
    def check(cls, value):
        if value is None:
            return value
        if type(value) is cls:
            return value
        try:
            return cls[cls._format_value(value)]
        except KeyError:
            return cls._missing_(value)


# Kraken supported symbols
class Symbol(_Enum):
    DASHEUR = 'DASHEUR'
    DASHUSD = 'DASHUSD'
    DASHXBT = 'DASHXBT'
    USDTZUSD = 'USDTUSD'
    XETCXETH = 'ETCETH'
    XETCXXBT = 'ETCXBT'
    XETCZEUR = 'ETCEUR'
    XETCZUSD = 'ETCUSD'
    XETHXXBT = 'ETHXBT'
    # XETHXXBT.d = 'ETHXBT.d'
    XETHZCAD = 'ETHCAD'
    # XETHZCAD.d = 'ETHCAD.d'
    XETHZEUR = 'ETHEUR'
    # XETHZEUR.d = 'ETHEUR.d'
    XETHZGBP = 'ETHGBP'
    # XETHZGBP.d = 'ETHGBP.d'
    XETHZJPY = 'ETHJPY'
    # XETHZJPY.d = 'ETHJPY.d'
    XETHZUSD = 'ETHUSD'
    # XETHZUSD.d = 'ETHUSD.d'
    XICNXETH = 'ICNETH'
    XICNXXBT = 'ICNXBT'
    XLTCXXBT = 'LTCXBT'
    XLTCZEUR = 'LTCEUR'
    XLTCZUSD = 'LTCUSD'
    XMLNXETH = 'MLNETH'
    XMLNXXBT = 'MLNXBT'
    XREPXETH = 'REPETH'
    XREPXXBT = 'REPXBT'
    XREPZEUR = 'REPEUR'
    XREPZUSD = 'REPUSD'
    XXBTZCAD = 'XBTCAD'
    # XXBTZCAD.d = 'XBTCAD.d'
    XXBTZEUR = 'XBTEUR'
    # XXBTZEUR.d = 'XBTEUR.d'
    XXBTZGBP = 'XBTGBP'
    # XXBTZGBP.d = 'XBTGBP.d'
    XXBTZJPY = 'XBTJPY'
    # XXBTZJPY.d = 'XBTJPY.d'
    XXBTZUSD = 'XBTUSD'
    # XXBTZUSD.d = 'XBTUSD.d'
    XXDGXXBT = 'XDGXBT'
    XXLMXXBT = 'XLMXBT'
    XXLMZEUR = 'XLMEUR'
    XXLMZUSD = 'XLMUSD'
    XXMRXXBT = 'XMRXBT'
    XXMRZEUR = 'XMREUR'
    XXMRZUSD = 'XMRUSD'
    XXRPXXBT = 'XRPXBT'
    XZECXXBT = 'ZECXBT'
    XZECZEUR = 'ZECEUR'
    XZECZUSD = 'ZECUSD'


# Kraken supported currencies
class Currency(_Enum):
    DASH = 'DASH'
    KFEE = 'FEE'
    USDT = 'USDT'
    XDAO = 'DAO'
    XETC = 'ETC'
    XETH = 'ETH'
    XICN = 'ICN'
    XLTC = 'LTC'
    XMLN = 'MLN'
    XNMC = 'NMC'
    XREP = 'REP'
    XXBT = 'XBT'
    XXDG = 'XDG'
    XXLM = 'XLM'
    XXMR = 'XMR'
    XXRP = 'XRP'
    XXVN = 'XVN'
    XZEC = 'ZEC'
    ZCAD = 'CAD'
    ZEUR = 'EUR'
    ZGBP = 'GBP'
    ZJPY = 'JPY'
    ZKRW = 'KRW'
    ZUSD = 'USD'