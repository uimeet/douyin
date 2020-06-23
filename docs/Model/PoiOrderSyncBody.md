# PoiOrderSyncBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mini_app** | [**PoiOrderSyncResponse**](PoiOrderSyncResponse.md) |  | [optional] 
**order_type** | **int** | 订单类型- 201 预约点餐订单, 202 餐厅预定订单, 203 餐厅排队订单, 9001 景区门票订单, 9101 团购券订单 | 
**date_time** | **int** | 发送请求的时间，精确到毫秒 | 
**order_detail** | **str** | 订单的细节，不同的订单业务有不同的结构体，请具体询问业务方字段结构 | 
**ext_shop_info** | [**ExtShopInfo**](ExtShopInfo.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

