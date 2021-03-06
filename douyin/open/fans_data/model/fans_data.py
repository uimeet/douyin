# coding: utf-8

"""

    获取用户的粉丝数据

    
"""

import pprint
import re  # noqa: F401

import six


class FansData(object):
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
        'all_fans_num': 'int',
        'gender_distributions': 'list[FansProfileDistribution]',
        'age_distributions': 'list[FansProfileDistribution]',
        'geographical_distributions': 'list[FansProfileDistribution]',
        'active_days_distributions': 'list[FansProfileDistribution]',
        'device_distributions': 'list[FansProfileDistribution]',
        'interest_distributions': 'list[FansProfileDistribution]',
        'flow_contributions': 'list[FansProfileFlowContribution]'
    }

    attribute_map = {
        'all_fans_num': 'all_fans_num',
        'gender_distributions': 'gender_distributions',
        'age_distributions': 'age_distributions',
        'geographical_distributions': 'geographical_distributions',
        'active_days_distributions': 'active_days_distributions',
        'device_distributions': 'device_distributions',
        'interest_distributions': 'interest_distributions',
        'flow_contributions': 'flow_contributions'
    }

    def __init__(self, all_fans_num=None, gender_distributions=None, age_distributions=None, geographical_distributions=None, active_days_distributions=None, device_distributions=None, interest_distributions=None, flow_contributions=None):  # noqa: E501
        """FansData - a model defined in Swagger"""  # noqa: E501
        self._all_fans_num = None
        self._gender_distributions = None
        self._age_distributions = None
        self._geographical_distributions = None
        self._active_days_distributions = None
        self._device_distributions = None
        self._interest_distributions = None
        self._flow_contributions = None
        self.discriminator = None
        self.all_fans_num = all_fans_num
        self.gender_distributions = gender_distributions
        self.age_distributions = age_distributions
        self.geographical_distributions = geographical_distributions
        self.active_days_distributions = active_days_distributions
        self.device_distributions = device_distributions
        self.interest_distributions = interest_distributions
        self.flow_contributions = flow_contributions

    @property
    def all_fans_num(self):
        """Gets the all_fans_num of this FansData.  # noqa: E501

        所有粉丝的数量  # noqa: E501

        :return: The all_fans_num of this FansData.  # noqa: E501
        :rtype: int
        """
        return self._all_fans_num

    @all_fans_num.setter
    def all_fans_num(self, all_fans_num):
        """Sets the all_fans_num of this FansData.

        所有粉丝的数量  # noqa: E501

        :param all_fans_num: The all_fans_num of this FansData.  # noqa: E501
        :type: int
        """
        if all_fans_num is None:
            raise ValueError("Invalid value for `all_fans_num`, must not be `None`")  # noqa: E501

        self._all_fans_num = all_fans_num

    @property
    def gender_distributions(self):
        """Gets the gender_distributions of this FansData.  # noqa: E501

        粉丝性别分布 item: [\"1\",\"2\"] (男:1,女:2)  # noqa: E501

        :return: The gender_distributions of this FansData.  # noqa: E501
        :rtype: list[FansProfileDistribution]
        """
        return self._gender_distributions

    @gender_distributions.setter
    def gender_distributions(self, gender_distributions):
        """Sets the gender_distributions of this FansData.

        粉丝性别分布 item: [\"1\",\"2\"] (男:1,女:2)  # noqa: E501

        :param gender_distributions: The gender_distributions of this FansData.  # noqa: E501
        :type: list[FansProfileDistribution]
        """
        if gender_distributions is None:
            raise ValueError("Invalid value for `gender_distributions`, must not be `None`")  # noqa: E501

        self._gender_distributions = gender_distributions

    @property
    def age_distributions(self):
        """Gets the age_distributions of this FansData.  # noqa: E501

        粉丝年龄分布 item: [\"<=25\",\"26-32\",\"33-39\",\"40-46\",\">46\"]  # noqa: E501

        :return: The age_distributions of this FansData.  # noqa: E501
        :rtype: list[FansProfileDistribution]
        """
        return self._age_distributions

    @age_distributions.setter
    def age_distributions(self, age_distributions):
        """Sets the age_distributions of this FansData.

        粉丝年龄分布 item: [\"<=25\",\"26-32\",\"33-39\",\"40-46\",\">46\"]  # noqa: E501

        :param age_distributions: The age_distributions of this FansData.  # noqa: E501
        :type: list[FansProfileDistribution]
        """
        if age_distributions is None:
            raise ValueError("Invalid value for `age_distributions`, must not be `None`")  # noqa: E501

        self._age_distributions = age_distributions

    @property
    def geographical_distributions(self):
        """Gets the geographical_distributions of this FansData.  # noqa: E501

        粉丝地域分布 item: [\"北京\",\"福建\",\"香港\"...]  # noqa: E501

        :return: The geographical_distributions of this FansData.  # noqa: E501
        :rtype: list[FansProfileDistribution]
        """
        return self._geographical_distributions

    @geographical_distributions.setter
    def geographical_distributions(self, geographical_distributions):
        """Sets the geographical_distributions of this FansData.

        粉丝地域分布 item: [\"北京\",\"福建\",\"香港\"...]  # noqa: E501

        :param geographical_distributions: The geographical_distributions of this FansData.  # noqa: E501
        :type: list[FansProfileDistribution]
        """
        if geographical_distributions is None:
            raise ValueError("Invalid value for `geographical_distributions`, must not be `None`")  # noqa: E501

        self._geographical_distributions = geographical_distributions

    @property
    def active_days_distributions(self):
        """Gets the active_days_distributions of this FansData.  # noqa: E501

        粉丝活跃天数分布 item: [\"0-1\",\"2-5\",\"6-10\",\"11-31\"]  # noqa: E501

        :return: The active_days_distributions of this FansData.  # noqa: E501
        :rtype: list[FansProfileDistribution]
        """
        return self._active_days_distributions

    @active_days_distributions.setter
    def active_days_distributions(self, active_days_distributions):
        """Sets the active_days_distributions of this FansData.

        粉丝活跃天数分布 item: [\"0-1\",\"2-5\",\"6-10\",\"11-31\"]  # noqa: E501

        :param active_days_distributions: The active_days_distributions of this FansData.  # noqa: E501
        :type: list[FansProfileDistribution]
        """
        if active_days_distributions is None:
            raise ValueError("Invalid value for `active_days_distributions`, must not be `None`")  # noqa: E501

        self._active_days_distributions = active_days_distributions

    @property
    def device_distributions(self):
        """Gets the device_distributions of this FansData.  # noqa: E501

        粉丝设备分布 item: [\"苹果\",\"华为\",\"三星\",\"小米\"...]  # noqa: E501

        :return: The device_distributions of this FansData.  # noqa: E501
        :rtype: list[FansProfileDistribution]
        """
        return self._device_distributions

    @device_distributions.setter
    def device_distributions(self, device_distributions):
        """Sets the device_distributions of this FansData.

        粉丝设备分布 item: [\"苹果\",\"华为\",\"三星\",\"小米\"...]  # noqa: E501

        :param device_distributions: The device_distributions of this FansData.  # noqa: E501
        :type: list[FansProfileDistribution]
        """
        if device_distributions is None:
            raise ValueError("Invalid value for `device_distributions`, must not be `None`")  # noqa: E501

        self._device_distributions = device_distributions

    @property
    def interest_distributions(self):
        """Gets the interest_distributions of this FansData.  # noqa: E501

        粉丝兴趣分布 item: [\"生活\"\",\"美食\",\"旅行\"...]  # noqa: E501

        :return: The interest_distributions of this FansData.  # noqa: E501
        :rtype: list[FansProfileDistribution]
        """
        return self._interest_distributions

    @interest_distributions.setter
    def interest_distributions(self, interest_distributions):
        """Sets the interest_distributions of this FansData.

        粉丝兴趣分布 item: [\"生活\"\",\"美食\",\"旅行\"...]  # noqa: E501

        :param interest_distributions: The interest_distributions of this FansData.  # noqa: E501
        :type: list[FansProfileDistribution]
        """
        if interest_distributions is None:
            raise ValueError("Invalid value for `interest_distributions`, must not be `None`")  # noqa: E501

        self._interest_distributions = interest_distributions

    @property
    def flow_contributions(self):
        """Gets the flow_contributions of this FansData.  # noqa: E501

        粉丝流量贡献 flow: [\"vv\",\"like_cnt\",\"comment_cnt\",\"share_video_cnt\"]  # noqa: E501

        :return: The flow_contributions of this FansData.  # noqa: E501
        :rtype: list[FansProfileFlowContribution]
        """
        return self._flow_contributions

    @flow_contributions.setter
    def flow_contributions(self, flow_contributions):
        """Sets the flow_contributions of this FansData.

        粉丝流量贡献 flow: [\"vv\",\"like_cnt\",\"comment_cnt\",\"share_video_cnt\"]  # noqa: E501

        :param flow_contributions: The flow_contributions of this FansData.  # noqa: E501
        :type: list[FansProfileFlowContribution]
        """
        if flow_contributions is None:
            raise ValueError("Invalid value for `flow_contributions`, must not be `None`")  # noqa: E501

        self._flow_contributions = flow_contributions

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
        if issubclass(FansData, dict):
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
        if not isinstance(other, FansData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
