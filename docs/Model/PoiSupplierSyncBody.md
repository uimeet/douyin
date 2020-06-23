# PoiSupplierSyncBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supplier_ext_id** | **str** | 接入方店铺id | 
**type** | [**SupplierType**](SupplierType.md) |  | 
**poi_id** | **str** | 抖音poi id, 三方如果使用高德poi id可以通过/poi/query/接口转换，其它三方poi id走poi匹配功能进行抖音poi id获取 | 
**status** | [**OnlineStatus**](OnlineStatus.md) |  | 
**name** | **str** | 店铺名称 | 
**images** | **list[str]** | 店铺图片 | 
**contact_phone** | **str** | 联系手机号 | [optional] 
**contact_tel** | **str** | 联系座机号 | [optional] 
**address** | **str** | 店铺地址 | [optional] 
**description** | **str** | 店铺介绍(&lt;&#x3D;500字) | [optional] 
**services** | [**list[PoiSupplierSyncServices]**](PoiSupplierSyncServices.md) | 店铺提供的服务列表 | [optional] 
**attributes** | [**SupplierAttributes**](SupplierAttributes.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

