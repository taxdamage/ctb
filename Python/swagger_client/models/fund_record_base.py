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

from swagger_client.models.funding_records import FundingRecords  # noqa: F401,E501


class FundRecordBase(object):
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
        'ret_code': 'float',
        'ret_msg': 'str',
        'ext_code': 'str',
        'ext_info': 'str',
        'result': 'list[FundingRecords]',
        'time_now': 'str'
    }

    attribute_map = {
        'ret_code': 'ret_code',
        'ret_msg': 'ret_msg',
        'ext_code': 'ext_code',
        'ext_info': 'ext_info',
        'result': 'result',
        'time_now': 'time_now'
    }

    def __init__(self, ret_code=None, ret_msg=None, ext_code=None, ext_info=None, result=None, time_now=None):  # noqa: E501
        """FundRecordBase - a model defined in Swagger"""  # noqa: E501

        self._ret_code = None
        self._ret_msg = None
        self._ext_code = None
        self._ext_info = None
        self._result = None
        self._time_now = None
        self.discriminator = None

        if ret_code is not None:
            self.ret_code = ret_code
        if ret_msg is not None:
            self.ret_msg = ret_msg
        if ext_code is not None:
            self.ext_code = ext_code
        if ext_info is not None:
            self.ext_info = ext_info
        if result is not None:
            self.result = result
        if time_now is not None:
            self.time_now = time_now

    @property
    def ret_code(self):
        """Gets the ret_code of this FundRecordBase.  # noqa: E501


        :return: The ret_code of this FundRecordBase.  # noqa: E501
        :rtype: float
        """
        return self._ret_code

    @ret_code.setter
    def ret_code(self, ret_code):
        """Sets the ret_code of this FundRecordBase.


        :param ret_code: The ret_code of this FundRecordBase.  # noqa: E501
        :type: float
        """

        self._ret_code = ret_code

    @property
    def ret_msg(self):
        """Gets the ret_msg of this FundRecordBase.  # noqa: E501


        :return: The ret_msg of this FundRecordBase.  # noqa: E501
        :rtype: str
        """
        return self._ret_msg

    @ret_msg.setter
    def ret_msg(self, ret_msg):
        """Sets the ret_msg of this FundRecordBase.


        :param ret_msg: The ret_msg of this FundRecordBase.  # noqa: E501
        :type: str
        """

        self._ret_msg = ret_msg

    @property
    def ext_code(self):
        """Gets the ext_code of this FundRecordBase.  # noqa: E501


        :return: The ext_code of this FundRecordBase.  # noqa: E501
        :rtype: str
        """
        return self._ext_code

    @ext_code.setter
    def ext_code(self, ext_code):
        """Sets the ext_code of this FundRecordBase.


        :param ext_code: The ext_code of this FundRecordBase.  # noqa: E501
        :type: str
        """

        self._ext_code = ext_code

    @property
    def ext_info(self):
        """Gets the ext_info of this FundRecordBase.  # noqa: E501


        :return: The ext_info of this FundRecordBase.  # noqa: E501
        :rtype: str
        """
        return self._ext_info

    @ext_info.setter
    def ext_info(self, ext_info):
        """Sets the ext_info of this FundRecordBase.


        :param ext_info: The ext_info of this FundRecordBase.  # noqa: E501
        :type: str
        """

        self._ext_info = ext_info

    @property
    def result(self):
        """Gets the result of this FundRecordBase.  # noqa: E501


        :return: The result of this FundRecordBase.  # noqa: E501
        :rtype: list[FundingRecords]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this FundRecordBase.


        :param result: The result of this FundRecordBase.  # noqa: E501
        :type: list[FundingRecords]
        """

        self._result = result

    @property
    def time_now(self):
        """Gets the time_now of this FundRecordBase.  # noqa: E501


        :return: The time_now of this FundRecordBase.  # noqa: E501
        :rtype: str
        """
        return self._time_now

    @time_now.setter
    def time_now(self, time_now):
        """Sets the time_now of this FundRecordBase.


        :param time_now: The time_now of this FundRecordBase.  # noqa: E501
        :type: str
        """

        self._time_now = time_now

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
        if issubclass(FundRecordBase, dict):
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
        if not isinstance(other, FundRecordBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
