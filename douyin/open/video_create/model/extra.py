# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    
"""

import pprint
import re  # noqa: F401

import six


class Extra(object):
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
        'log_id': 'str',
        'now': 'int'
    }

    attribute_map = {
        'log_id': 'log_id',
        'now': 'now'
    }

    def __init__(self, log_id=None, now=None):  # noqa: E501
        """Extra - a model defined in Swagger"""  # noqa: E501
        self._log_id = None
        self._now = None
        self.discriminator = None
        if log_id is not None:
            self.log_id = log_id
        if now is not None:
            self.now = now

    @property
    def log_id(self):
        """Gets the log_id of this Extra.  # noqa: E501


        :return: The log_id of this Extra.  # noqa: E501
        :rtype: str
        """
        return self._log_id

    @log_id.setter
    def log_id(self, log_id):
        """Sets the log_id of this Extra.


        :param log_id: The log_id of this Extra.  # noqa: E501
        :type: str
        """

        self._log_id = log_id

    @property
    def now(self):
        """Gets the now of this Extra.  # noqa: E501


        :return: The now of this Extra.  # noqa: E501
        :rtype: int
        """
        return self._now

    @now.setter
    def now(self, now):
        """Sets the now of this Extra.


        :param now: The now of this Extra.  # noqa: E501
        :type: int
        """

        self._now = now

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
        if issubclass(Extra, dict):
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
        if not isinstance(other, Extra):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
