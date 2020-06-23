###PoiSkuApi_poi_ext_hotel_sku_get
```python
from __future__ import print_function
import time
import douyin.open.poi.product
from douyin.open.poi.product.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.poi.product.PoiSkuApi()
spu_ext_id = ['[\"y0001\",\"y0002\"]'] # list[str] | 接入方SPU ID 列表
start_date = '20191001' # str | 拉取价格时间区间[start_date, end_date)
end_date = '20191007' # str | 拉取价格时间区间[start_date, end_date)

try:
    # sku拉取(该接口由接入方实现)
    api_response = api_instance.poi_ext_hotel_sku_get(spu_ext_id, start_date, end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiSkuApi->poi_ext_hotel_sku_get: %s\n" % e)
```
