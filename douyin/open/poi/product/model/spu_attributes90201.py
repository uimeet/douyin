# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    
"""

import pprint
import re  # noqa: F401

import six


class SpuAttributes90201(object):
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
        'time_type': 'int',
        'time': 'str'
    }

    attribute_map = {
        'time_type': 'time_type',
        'time': 'time'
    }

    def __init__(self, time_type=None, time=None):  # noqa: E501
        """SpuAttributes90201 - a model defined in Swagger"""  # noqa: E501
        self._time_type = None
        self._time = None
        self.discriminator = None
        self.time_type = time_type
        if time is not None:
            self.time = time

    @property
    def time_type(self):
        """Gets the time_type of this SpuAttributes90201.  # noqa: E501

        时间格式 1-最早可订今日，2-最早可订明日, 3-最早可订MM月dd日, 4-HH:mm前可订当日, 5-需提前x天预订  # noqa: E501

        :return: The time_type of this SpuAttributes90201.  # noqa: E501
        :rtype: int
        """
        return self._time_type

    @time_type.setter
    def time_type(self, time_type):
        """Sets the time_type of this SpuAttributes90201.

        时间格式 1-最早可订今日，2-最早可订明日, 3-最早可订MM月dd日, 4-HH:mm前可订当日, 5-需提前x天预订  # noqa: E501

        :param time_type: The time_type of this SpuAttributes90201.  # noqa: E501
        :type: int
        """
        if time_type is None:
            raise ValueError("Invalid value for `time_type`, must not be `None`")  # noqa: E501
        allowed_values = [1, 2, 3, 4, 5]  # noqa: E501
        if time_type not in allowed_values:
            raise ValueError(
                "Invalid value for `time_type` ({0}), must be one of {1}"  # noqa: E501
                .format(time_type, allowed_values)
            )

        self._time_type = time_type

    @property
    def time(self):
        """Gets the time of this SpuAttributes90201.  # noqa: E501

        time_type为3时该字段必选(yyyyMMdd格式)，time_type为4时该字段必选(HH:mm格式), time_type为5时该字段必选(x格式)  # noqa: E501

        :return: The time of this SpuAttributes90201.  # noqa: E501
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this SpuAttributes90201.

        time_type为3时该字段必选(yyyyMMdd格式)，time_type为4时该字段必选(HH:mm格式), time_type为5时该字段必选(x格式)  # noqa: E501

        :param time: The time of this SpuAttributes90201.  # noqa: E501
        :type: str
        """

        self._time = time

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
        if issubclass(SpuAttributes90201, dict):
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
        if not isinstance(other, SpuAttributes90201):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
