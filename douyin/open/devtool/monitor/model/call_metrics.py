# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    
"""

import pprint
import re  # noqa: F401

import six


class CallMetrics(object):
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
        'date_time': 'str',
        'scope': 'str',
        'interface': 'str',
        'pv': 'int'
    }

    attribute_map = {
        'date_time': 'date_time',
        'scope': 'scope',
        'interface': 'interface',
        'pv': 'pv'
    }

    def __init__(self, date_time=None, scope=None, interface=None, pv=None):  # noqa: E501
        """CallMetrics - a model defined in Swagger"""  # noqa: E501
        self._date_time = None
        self._scope = None
        self._interface = None
        self._pv = None
        self.discriminator = None
        self.date_time = date_time
        if scope is not None:
            self.scope = scope
        if interface is not None:
            self.interface = interface
        self.pv = pv

    @property
    def date_time(self):
        """Gets the date_time of this CallMetrics.  # noqa: E501

        时间  # noqa: E501

        :return: The date_time of this CallMetrics.  # noqa: E501
        :rtype: str
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this CallMetrics.

        时间  # noqa: E501

        :param date_time: The date_time of this CallMetrics.  # noqa: E501
        :type: str
        """
        if date_time is None:
            raise ValueError("Invalid value for `date_time`, must not be `None`")  # noqa: E501

        self._date_time = date_time

    @property
    def scope(self):
        """Gets the scope of this CallMetrics.  # noqa: E501

        scope  # noqa: E501

        :return: The scope of this CallMetrics.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this CallMetrics.

        scope  # noqa: E501

        :param scope: The scope of this CallMetrics.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def interface(self):
        """Gets the interface of this CallMetrics.  # noqa: E501

        访问链接  # noqa: E501

        :return: The interface of this CallMetrics.  # noqa: E501
        :rtype: str
        """
        return self._interface

    @interface.setter
    def interface(self, interface):
        """Sets the interface of this CallMetrics.

        访问链接  # noqa: E501

        :param interface: The interface of this CallMetrics.  # noqa: E501
        :type: str
        """

        self._interface = interface

    @property
    def pv(self):
        """Gets the pv of this CallMetrics.  # noqa: E501

        pv  # noqa: E501

        :return: The pv of this CallMetrics.  # noqa: E501
        :rtype: int
        """
        return self._pv

    @pv.setter
    def pv(self, pv):
        """Sets the pv of this CallMetrics.

        pv  # noqa: E501

        :param pv: The pv of this CallMetrics.  # noqa: E501
        :type: int
        """
        if pv is None:
            raise ValueError("Invalid value for `pv`, must not be `None`")  # noqa: E501

        self._pv = pv

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
        if issubclass(CallMetrics, dict):
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
        if not isinstance(other, CallMetrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
