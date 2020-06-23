# coding: utf-8

"""

    通过头条视频id批量获取已分享视频数据信息

    
"""

import pprint
import re  # noqa: F401

import six


class ToutiaoVideoDataResponseData(object):
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
        'error_code': 'ErrorCode',
        'description': 'Description',
        'list': 'list[ToutiaoVideo]'
    }

    attribute_map = {
        'error_code': 'error_code',
        'description': 'description',
        'list': 'list'
    }

    def __init__(self, error_code=None, description=None, list=None):  # noqa: E501
        """ToutiaoVideoDataResponseData - a model defined in Swagger"""  # noqa: E501
        self._error_code = None
        self._description = None
        self._list = None
        self.discriminator = None
        self.error_code = error_code
        self.description = description
        if list is not None:
            self.list = list

    @property
    def error_code(self):
        """Gets the error_code of this ToutiaoVideoDataResponseData.  # noqa: E501


        :return: The error_code of this ToutiaoVideoDataResponseData.  # noqa: E501
        :rtype: ErrorCode
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ToutiaoVideoDataResponseData.


        :param error_code: The error_code of this ToutiaoVideoDataResponseData.  # noqa: E501
        :type: ErrorCode
        """
        if error_code is None:
            raise ValueError("Invalid value for `error_code`, must not be `None`")  # noqa: E501

        self._error_code = error_code

    @property
    def description(self):
        """Gets the description of this ToutiaoVideoDataResponseData.  # noqa: E501


        :return: The description of this ToutiaoVideoDataResponseData.  # noqa: E501
        :rtype: Description
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ToutiaoVideoDataResponseData.


        :param description: The description of this ToutiaoVideoDataResponseData.  # noqa: E501
        :type: Description
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def list(self):
        """Gets the list of this ToutiaoVideoDataResponseData.  # noqa: E501


        :return: The list of this ToutiaoVideoDataResponseData.  # noqa: E501
        :rtype: list[ToutiaoVideo]
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this ToutiaoVideoDataResponseData.


        :param list: The list of this ToutiaoVideoDataResponseData.  # noqa: E501
        :type: list[ToutiaoVideo]
        """

        self._list = list

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
        if issubclass(ToutiaoVideoDataResponseData, dict):
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
        if not isinstance(other, ToutiaoVideoDataResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
