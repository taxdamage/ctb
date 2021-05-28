# coding: utf-8

"""
    Bybit API

    ## REST API for the Bybit Exchange. Base URI: [https://api.bybit.com]    # noqa: E501

    OpenAPI spec version: 0.2.11
    Contact: support@bybit.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TradingStopRes(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'float',
        'user_id': 'float',
        'symbol': 'str',
        'side': 'str',
        'size': 'float',
        'position_value': 'float',
        'entry_price': 'float',
        'risk_id': 'float',
        'auto_add_margin': 'float',
        'leverage': 'float',
        'position_margin': 'float',
        'liq_price': 'float',
        'bust_price': 'float',
        'occ_closing_fee': 'float',
        'occ_funding_fee': 'float',
        'take_profit': 'float',
        'stop_loss': 'float',
        'position_status': 'str',
        'deleverage_indicator': 'float',
        'oc_calc_data': 'str',
        'order_margin': 'float',
        'wallet_balance': 'float',
        'realised_pnl': 'float',
        'cum_realised_pnl': 'float',
        'cum_commission': 'float',
        'cross_seq': 'float',
        'position_seq': 'float',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'user_id': 'user_id',
        'symbol': 'symbol',
        'side': 'side',
        'size': 'size',
        'position_value': 'position_value',
        'entry_price': 'entry_price',
        'risk_id': 'risk_id',
        'auto_add_margin': 'auto_add_margin',
        'leverage': 'leverage',
        'position_margin': 'position_margin',
        'liq_price': 'liq_price',
        'bust_price': 'bust_price',
        'occ_closing_fee': 'occ_closing_fee',
        'occ_funding_fee': 'occ_funding_fee',
        'take_profit': 'take_profit',
        'stop_loss': 'stop_loss',
        'position_status': 'position_status',
        'deleverage_indicator': 'deleverage_indicator',
        'oc_calc_data': 'oc_calc_data',
        'order_margin': 'order_margin',
        'wallet_balance': 'wallet_balance',
        'realised_pnl': 'realised_pnl',
        'cum_realised_pnl': 'cum_realised_pnl',
        'cum_commission': 'cum_commission',
        'cross_seq': 'cross_seq',
        'position_seq': 'position_seq',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, user_id=None, symbol=None, side=None, size=None, position_value=None, entry_price=None, risk_id=None, auto_add_margin=None, leverage=None, position_margin=None, liq_price=None, bust_price=None, occ_closing_fee=None, occ_funding_fee=None, take_profit=None, stop_loss=None, position_status=None, deleverage_indicator=None, oc_calc_data=None, order_margin=None, wallet_balance=None, realised_pnl=None, cum_realised_pnl=None, cum_commission=None, cross_seq=None, position_seq=None, created_at=None, updated_at=None):  # noqa: E501
        """TradingStopRes - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._user_id = None
        self._symbol = None
        self._side = None
        self._size = None
        self._position_value = None
        self._entry_price = None
        self._risk_id = None
        self._auto_add_margin = None
        self._leverage = None
        self._position_margin = None
        self._liq_price = None
        self._bust_price = None
        self._occ_closing_fee = None
        self._occ_funding_fee = None
        self._take_profit = None
        self._stop_loss = None
        self._position_status = None
        self._deleverage_indicator = None
        self._oc_calc_data = None
        self._order_margin = None
        self._wallet_balance = None
        self._realised_pnl = None
        self._cum_realised_pnl = None
        self._cum_commission = None
        self._cross_seq = None
        self._position_seq = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user_id is not None:
            self.user_id = user_id
        if symbol is not None:
            self.symbol = symbol
        if side is not None:
            self.side = side
        if size is not None:
            self.size = size
        if position_value is not None:
            self.position_value = position_value
        if entry_price is not None:
            self.entry_price = entry_price
        if risk_id is not None:
            self.risk_id = risk_id
        if auto_add_margin is not None:
            self.auto_add_margin = auto_add_margin
        if leverage is not None:
            self.leverage = leverage
        if position_margin is not None:
            self.position_margin = position_margin
        if liq_price is not None:
            self.liq_price = liq_price
        if bust_price is not None:
            self.bust_price = bust_price
        if occ_closing_fee is not None:
            self.occ_closing_fee = occ_closing_fee
        if occ_funding_fee is not None:
            self.occ_funding_fee = occ_funding_fee
        if take_profit is not None:
            self.take_profit = take_profit
        if stop_loss is not None:
            self.stop_loss = stop_loss
        if position_status is not None:
            self.position_status = position_status
        if deleverage_indicator is not None:
            self.deleverage_indicator = deleverage_indicator
        if oc_calc_data is not None:
            self.oc_calc_data = oc_calc_data
        if order_margin is not None:
            self.order_margin = order_margin
        if wallet_balance is not None:
            self.wallet_balance = wallet_balance
        if realised_pnl is not None:
            self.realised_pnl = realised_pnl
        if cum_realised_pnl is not None:
            self.cum_realised_pnl = cum_realised_pnl
        if cum_commission is not None:
            self.cum_commission = cum_commission
        if cross_seq is not None:
            self.cross_seq = cross_seq
        if position_seq is not None:
            self.position_seq = position_seq
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this TradingStopRes.  # noqa: E501


        :return: The id of this TradingStopRes.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TradingStopRes.


        :param id: The id of this TradingStopRes.  # noqa: E501
        :type: float
        """

        self._id = id

    @property
    def user_id(self):
        """Gets the user_id of this TradingStopRes.  # noqa: E501


        :return: The user_id of this TradingStopRes.  # noqa: E501
        :rtype: float
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this TradingStopRes.


        :param user_id: The user_id of this TradingStopRes.  # noqa: E501
        :type: float
        """

        self._user_id = user_id

    @property
    def symbol(self):
        """Gets the symbol of this TradingStopRes.  # noqa: E501


        :return: The symbol of this TradingStopRes.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this TradingStopRes.


        :param symbol: The symbol of this TradingStopRes.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def side(self):
        """Gets the side of this TradingStopRes.  # noqa: E501


        :return: The side of this TradingStopRes.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this TradingStopRes.


        :param side: The side of this TradingStopRes.  # noqa: E501
        :type: str
        """

        self._side = side

    @property
    def size(self):
        """Gets the size of this TradingStopRes.  # noqa: E501


        :return: The size of this TradingStopRes.  # noqa: E501
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this TradingStopRes.


        :param size: The size of this TradingStopRes.  # noqa: E501
        :type: float
        """

        self._size = size

    @property
    def position_value(self):
        """Gets the position_value of this TradingStopRes.  # noqa: E501


        :return: The position_value of this TradingStopRes.  # noqa: E501
        :rtype: float
        """
        return self._position_value

    @position_value.setter
    def position_value(self, position_value):
        """Sets the position_value of this TradingStopRes.


        :param position_value: The position_value of this TradingStopRes.  # noqa: E501
        :type: float
        """

        self._position_value = position_value

    @property
    def entry_price(self):
        """Gets the entry_price of this TradingStopRes.  # noqa: E501


        :return: The entry_price of this TradingStopRes.  # noqa: E501
        :rtype: float
        """
        return self._entry_price

    @entry_price.setter
    def entry_price(self, entry_price):
        """Sets the entry_price of this TradingStopRes.


        :param entry_price: The entry_price of this TradingStopRes.  # noqa: E501
        :type: float
        """

        self._entry_price = entry_price

    @property
    def risk_id(self):
        """Gets the risk_id of this TradingStopRes.  # noqa: E501


        :return: The risk_id of this TradingStopRes.  # noqa: E501
        :rtype: float
        """
        return self._risk_id

    @risk_id.setter
    def risk_id(self, risk_id):
        """Sets the risk_id of this TradingStopRes.


        :param risk_id: The risk_id of this TradingStopRes.  # noqa: E501
        :type: float
        """

        self._risk_id = risk_id

    @property
    def auto_add_margin(self):
        """Gets the auto_add_margin of this TradingStopRes.  # noqa: E501


        :return: The auto_add_margin of this TradingStopRes.  # noqa: E501
        :rtype: float
        """
        return self._auto_add_margin

    @auto_add_margin.setter
    def auto_add_margin(self, auto_add_margin):
        """Sets the auto_add_margin of this TradingStopRes.


        :param auto_add_margin: The auto_add_margin of this TradingStopRes.  # noqa: E501
        :type: float
        """

        self._auto_add_margin = auto_add_margin

    @property
    def leverage(self):
        """Gets the leverage of this TradingStopRes.  # noqa: E501


        :return: The leverage of this TradingStopRes.  # noqa: E501
        :rtype: float
        """
        return self._leverage

    @leverage.setter
    def leverage(self, leverage):
        """Sets the leverage of this TradingStopRes.


        :param leverage: The leverage of this TradingStopRes.  # noqa: E501
        :type: float
        """

        self._leverage = leverage

    @property
    def position_margin(self):
        """Gets the position_margin of this TradingStopRes.  # noqa: E501


        :return: The position_margin of this TradingStopRes.  # noqa: E501
        :rtype: float
        """
        return self._position_margin

    @position_margin.setter
    def position_margin(self, position_margin):
        """Sets the position_margin of this TradingStopRes.


        :param position_margin: The position_margin of this TradingStopRes.  # noqa: E501
        :type: float
        """

        self._position_margin = position_margin

    @property
    def liq_price(self):
        """Gets the liq_price of this TradingStopRes.  # noqa: E501


        :return: The liq_price of this TradingStopRes.  # noqa: E501
        :rtype: float
        """
        return self._liq_price

    @liq_price.setter
    def liq_price(self, liq_price):
        """Sets the liq_price of this TradingStopRes.


        :param liq_price: The liq_price of this TradingStopRes.  # noqa: E501
        :type: float
        """

        self._liq_price = liq_price

    @property
    def bust_price(self):
        """Gets the bust_price of this TradingStopRes.  # noqa: E501


        :return: The bust_price of this TradingStopRes.  # noqa: E501
        :rtype: float
        """
        return self._bust_price

    @bust_price.setter
    def bust_price(self, bust_price):
        """Sets the bust_price of this TradingStopRes.


        :param bust_price: The bust_price of this TradingStopRes.  # noqa: E501
        :type: float
        """

        self._bust_price = bust_price

    @property
    def occ_closing_fee(self):
        """Gets the occ_closing_fee of this TradingStopRes.  # noqa: E501


        :return: The occ_closing_fee of this TradingStopRes.  # noqa: E501
        :rtype: float
        """
        return self._occ_closing_fee

    @occ_closing_fee.setter
    def occ_closing_fee(self, occ_closing_fee):
        """Sets the occ_closing_fee of this TradingStopRes.


        :param occ_closing_fee: The occ_closing_fee of this TradingStopRes.  # noqa: E501
        :type: float
        """

        self._occ_closing_fee = occ_closing_fee

    @property
    def occ_funding_fee(self):
        """Gets the occ_funding_fee of this TradingStopRes.  # noqa: E501


        :return: The occ_funding_fee of this TradingStopRes.  # noqa: E501
        :rtype: float
        """
        return self._occ_funding_fee

    @occ_funding_fee.setter
    def occ_funding_fee(self, occ_funding_fee):
        """Sets the occ_funding_fee of this TradingStopRes.


        :param occ_funding_fee: The occ_funding_fee of this TradingStopRes.  # noqa: E501
        :type: float
        """

        self._occ_funding_fee = occ_funding_fee

    @property
    def take_profit(self):
        """Gets the take_profit of this TradingStopRes.  # noqa: E501


        :return: The take_profit of this TradingStopRes.  # noqa: E501
        :rtype: float
        """
        return self._take_profit

    @take_profit.setter
    def take_profit(self, take_profit):
        """Sets the take_profit of this TradingStopRes.


        :param take_profit: The take_profit of this TradingStopRes.  # noqa: E501
        :type: float
        """

        self._take_profit = take_profit

    @property
    def stop_loss(self):
        """Gets the stop_loss of this TradingStopRes.  # noqa: E501


        :return: The stop_loss of this TradingStopRes.  # noqa: E501
        :rtype: float
        """
        return self._stop_loss

    @stop_loss.setter
    def stop_loss(self, stop_loss):
        """Sets the stop_loss of this TradingStopRes.


        :param stop_loss: The stop_loss of this TradingStopRes.  # noqa: E501
        :type: float
        """

        self._stop_loss = stop_loss

    @property
    def position_status(self):
        """Gets the position_status of this TradingStopRes.  # noqa: E501


        :return: The position_status of this TradingStopRes.  # noqa: E501
        :rtype: str
        """
        return self._position_status

    @position_status.setter
    def position_status(self, position_status):
        """Sets the position_status of this TradingStopRes.


        :param position_status: The position_status of this TradingStopRes.  # noqa: E501
        :type: str
        """

        self._position_status = position_status

    @property
    def deleverage_indicator(self):
        """Gets the deleverage_indicator of this TradingStopRes.  # noqa: E501


        :return: The deleverage_indicator of this TradingStopRes.  # noqa: E501
        :rtype: float
        """
        return self._deleverage_indicator

    @deleverage_indicator.setter
    def deleverage_indicator(self, deleverage_indicator):
        """Sets the deleverage_indicator of this TradingStopRes.


        :param deleverage_indicator: The deleverage_indicator of this TradingStopRes.  # noqa: E501
        :type: float
        """

        self._deleverage_indicator = deleverage_indicator

    @property
    def oc_calc_data(self):
        """Gets the oc_calc_data of this TradingStopRes.  # noqa: E501


        :return: The oc_calc_data of this TradingStopRes.  # noqa: E501
        :rtype: str
        """
        return self._oc_calc_data

    @oc_calc_data.setter
    def oc_calc_data(self, oc_calc_data):
        """Sets the oc_calc_data of this TradingStopRes.


        :param oc_calc_data: The oc_calc_data of this TradingStopRes.  # noqa: E501
        :type: str
        """

        self._oc_calc_data = oc_calc_data

    @property
    def order_margin(self):
        """Gets the order_margin of this TradingStopRes.  # noqa: E501


        :return: The order_margin of this TradingStopRes.  # noqa: E501
        :rtype: float
        """
        return self._order_margin

    @order_margin.setter
    def order_margin(self, order_margin):
        """Sets the order_margin of this TradingStopRes.


        :param order_margin: The order_margin of this TradingStopRes.  # noqa: E501
        :type: float
        """

        self._order_margin = order_margin

    @property
    def wallet_balance(self):
        """Gets the wallet_balance of this TradingStopRes.  # noqa: E501


        :return: The wallet_balance of this TradingStopRes.  # noqa: E501
        :rtype: float
        """
        return self._wallet_balance

    @wallet_balance.setter
    def wallet_balance(self, wallet_balance):
        """Sets the wallet_balance of this TradingStopRes.


        :param wallet_balance: The wallet_balance of this TradingStopRes.  # noqa: E501
        :type: float
        """

        self._wallet_balance = wallet_balance

    @property
    def realised_pnl(self):
        """Gets the realised_pnl of this TradingStopRes.  # noqa: E501


        :return: The realised_pnl of this TradingStopRes.  # noqa: E501
        :rtype: float
        """
        return self._realised_pnl

    @realised_pnl.setter
    def realised_pnl(self, realised_pnl):
        """Sets the realised_pnl of this TradingStopRes.


        :param realised_pnl: The realised_pnl of this TradingStopRes.  # noqa: E501
        :type: float
        """

        self._realised_pnl = realised_pnl

    @property
    def cum_realised_pnl(self):
        """Gets the cum_realised_pnl of this TradingStopRes.  # noqa: E501


        :return: The cum_realised_pnl of this TradingStopRes.  # noqa: E501
        :rtype: float
        """
        return self._cum_realised_pnl

    @cum_realised_pnl.setter
    def cum_realised_pnl(self, cum_realised_pnl):
        """Sets the cum_realised_pnl of this TradingStopRes.


        :param cum_realised_pnl: The cum_realised_pnl of this TradingStopRes.  # noqa: E501
        :type: float
        """

        self._cum_realised_pnl = cum_realised_pnl

    @property
    def cum_commission(self):
        """Gets the cum_commission of this TradingStopRes.  # noqa: E501


        :return: The cum_commission of this TradingStopRes.  # noqa: E501
        :rtype: float
        """
        return self._cum_commission

    @cum_commission.setter
    def cum_commission(self, cum_commission):
        """Sets the cum_commission of this TradingStopRes.


        :param cum_commission: The cum_commission of this TradingStopRes.  # noqa: E501
        :type: float
        """

        self._cum_commission = cum_commission

    @property
    def cross_seq(self):
        """Gets the cross_seq of this TradingStopRes.  # noqa: E501


        :return: The cross_seq of this TradingStopRes.  # noqa: E501
        :rtype: float
        """
        return self._cross_seq

    @cross_seq.setter
    def cross_seq(self, cross_seq):
        """Sets the cross_seq of this TradingStopRes.


        :param cross_seq: The cross_seq of this TradingStopRes.  # noqa: E501
        :type: float
        """

        self._cross_seq = cross_seq

    @property
    def position_seq(self):
        """Gets the position_seq of this TradingStopRes.  # noqa: E501


        :return: The position_seq of this TradingStopRes.  # noqa: E501
        :rtype: float
        """
        return self._position_seq

    @position_seq.setter
    def position_seq(self, position_seq):
        """Sets the position_seq of this TradingStopRes.


        :param position_seq: The position_seq of this TradingStopRes.  # noqa: E501
        :type: float
        """

        self._position_seq = position_seq

    @property
    def created_at(self):
        """Gets the created_at of this TradingStopRes.  # noqa: E501


        :return: The created_at of this TradingStopRes.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TradingStopRes.


        :param created_at: The created_at of this TradingStopRes.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this TradingStopRes.  # noqa: E501


        :return: The updated_at of this TradingStopRes.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this TradingStopRes.


        :param updated_at: The updated_at of this TradingStopRes.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(TradingStopRes, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TradingStopRes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
