# OauthAccessTokenResponseData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | [**ErrorCode**](ErrorCode.md) |  | [optional] 
**description** | [**Description**](Description.md) |  | [optional] 
**access_token** | **str** | 接口调用凭证 | [optional] 
**expires_in** | **str** | access_token接口调用凭证超时时间，单位（秒 | [optional] 
**refresh_token** | **str** | 用户刷新access_token | [optional] 
**open_id** | **str** | 授权用户唯一标识 | [optional] 
**scope** | **str** | 用户授权的作用域(Scope)，使用逗号（,）分隔，开放平台几乎几乎每个接口都需要特定的Scope。  | [optional] 
**unionid** | **str** | 当且仅当该网站应用已获得该用户的userinfo授权时，才会出现该字段。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

