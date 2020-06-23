# VideoCreateBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**video_id** | **str** | video_id, 通过/video/upload/接口得到。注意每次调用/video/create/都要调用/video/upload/生成新的video_id。 | 
**text** | **str** | 视频标题， 可以带话题,@用户。 如title1#话题1 #话题2 @openid1  注意：   1. 话题审核依旧遵循抖音的审核逻辑，强烈建议第三方谨慎拟定话题名称，避免强导流行为。  | [optional] 
**poi_id** | **str** | 地理位置id | [optional] 
**poi_name** | **str** | 地理位置名称 | [optional] 
**micro_app_id** | **str** | 小程序id | [optional] 
**micro_app_title** | **str** | 小程序标题 | [optional] 
**micro_app_url** | **str** | 吊起小程序时的参数 | [optional] 
**cover_tsp** | **float** | 将传入的指定时间点对应帧设置为视频封面（单位：秒） | [optional] 
**at_users** | **list[str]** | 如果需要at其他用户。将text中@nickname对应的open_id放到这里。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

