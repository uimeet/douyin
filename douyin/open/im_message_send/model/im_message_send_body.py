# coding: utf-8

"""
    发送消息

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    
"""

import pprint
import re  # noqa: F401

import six


class ImMessageSendBody(object):
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
        'to_user_id': 'str',
        'message_type': 'str',
        'content': 'str'
    }

    attribute_map = {
        'to_user_id': 'to_user_id',
        'message_type': 'message_type',
        'content': 'content'
    }

    def __init__(self, to_user_id=None, message_type=None, content=None):  # noqa: E501
        """ImMessageSendBody - a model defined in Swagger"""  # noqa: E501
        self._to_user_id = None
        self._message_type = None
        self._content = None
        self.discriminator = None
        self.to_user_id = to_user_id
        self.message_type = message_type
        self.content = content

    @property
    def to_user_id(self):
        """Gets the to_user_id of this ImMessageSendBody.  # noqa: E501

        发送消息的接收方openid  # noqa: E501

        :return: The to_user_id of this ImMessageSendBody.  # noqa: E501
        :rtype: str
        """
        return self._to_user_id

    @to_user_id.setter
    def to_user_id(self, to_user_id):
        """Sets the to_user_id of this ImMessageSendBody.

        发送消息的接收方openid  # noqa: E501

        :param to_user_id: The to_user_id of this ImMessageSendBody.  # noqa: E501
        :type: str
        """
        if to_user_id is None:
            raise ValueError("Invalid value for `to_user_id`, must not be `None`")  # noqa: E501

        self._to_user_id = to_user_id

    @property
    def message_type(self):
        """Gets the message_type of this ImMessageSendBody.  # noqa: E501

        消息内容格式:   * `text` - 文本消息   * `image` - 图片消息   # noqa: E501

        :return: The message_type of this ImMessageSendBody.  # noqa: E501
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """Sets the message_type of this ImMessageSendBody.

        消息内容格式:   * `text` - 文本消息   * `image` - 图片消息   # noqa: E501

        :param message_type: The message_type of this ImMessageSendBody.  # noqa: E501
        :type: str
        """
        if message_type is None:
            raise ValueError("Invalid value for `message_type`, must not be `None`")  # noqa: E501
        allowed_values = ["text", "image"]  # noqa: E501
        if message_type not in allowed_values:
            raise ValueError(
                "Invalid value for `message_type` ({0}), must be one of {1}"  # noqa: E501
                .format(message_type, allowed_values)
            )

        self._message_type = message_type

    @property
    def content(self):
        """Gets the content of this ImMessageSendBody.  # noqa: E501

        文本内容 或 素材id  # noqa: E501

        :return: The content of this ImMessageSendBody.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ImMessageSendBody.

        文本内容 或 素材id  # noqa: E501

        :param content: The content of this ImMessageSendBody.  # noqa: E501
        :type: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

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
        if issubclass(ImMessageSendBody, dict):
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
        if not isinstance(other, ImMessageSendBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
