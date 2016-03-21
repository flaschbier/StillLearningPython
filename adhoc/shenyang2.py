from bs4 import BeautifulSoup
import re
import json

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<td id="cur_o3" class="tdcur" style="font-weight:bold;font-size:11px;" align="center">2</td>
</script><script type="text/javascript">
try {
if (isMapOpened == "open") {
mapInitWithData([{"aqi":"294","city":"D\u014dngru\u01cen, Shenyang","x":1249,"g":["41.7089","123.439"]},{"aqi":"263","city":"Liaoyang","extra":1,"x":4347,"g":["41.267244","123.236944"]},{"aqi":"263","city":"Ch\u00e9nli\u00e1ox\u012b l\u00f9, Shenyang","x":8755,"g":["41.7347","123.2444"]},{"aqi":"255","city":"Tieling","extra":1,"x":4346,"g":["42.22297","123.726163"]},{"aqi":"249","city":"h\u00fan n\u00e1n d\u014dng l\u00f9, Shenyang , Shenyang","x":5218,"g":["41.7561","123.535"]},{"aqi":"238","city":"Shenyang US Consulate","lvl":1,"x":496,"g":["41.7832349","123.4267266"]},{"aqi":"238","city":"Xiaoheyan, Shenyang","x":1254,"g":["41.7775","123.478"]},{"aqi":"219","city":"Liaoning University, Shenyang","x":1257,"g":["41.9228","123.3783"]},{"aqi":"193","city":"wenhua street, Shenyang , Shenyang","x":5215,"g":["41.765","123.41"]},{"aqi":"191","city":"Shenyang","x":1473,"g":["41.805698","123.431475"]},{"aqi":"191","city":"Taiyuan Street, Shenyang","x":1255,"g":["41.7972","123.3997"]},{"aqi":"189","city":"Shenfu new town, Fushun","x":4355,"g":["41.8417","123.7117"]},{"aqi":"188","city":"Wanghua district, Fushun , Fushun","extra":1,"x":5240,"g":["41.8469","123.8100"]},{"aqi":"188","city":"Fushun","extra":1,"x":1476,"g":["41.880872","123.957208"]},{"aqi":"188","city":"j\u012bnsh\u0101 ji\u0101ng l\u00f9 b\u011bi, Tieling , Tieling","extra":1,"x":5203,"g":["42.2217","123.7153"]},{"aqi":"182","city":"Tanglin Road , Shenyang , Shenyang","x":5216,"g":["41.8336","123.542"]},{"aqi":"179","city":"Caitun, Benxi","extra":1,"x":4364,"g":["41.3047","123.7308"]},{"aqi":"176","city":"Xihu, Benxi","extra":1,"x":4365,"g":["41.3369","123.7528"]},{"aqi":"172","city":"Xinfu district, Fushun , Fushun","extra":1,"x":5237,"g":["41.8594","123.9000"]},{"aqi":"170","city":"Weining, Benxi","extra":1,"x":4361,"g":["41.3472","123.8142"]},{"aqi":"162","city":"Shuncheng district, Fushun , Fushun","extra":1,"x":5239,"g":["41.883375","123.94504"]},{"aqi":"161","city":"y\u00f9n\u00f3ng l\u00f9, Shenyang","x":8756,"g":["41.9086","123.5953"]},{"aqi":"151","city":"Dongzhou district, Fushun , Fushun","extra":1,"x":5238,"g":["41.8625","124.0383"]},{"aqi":"122","city":"Dahuofang reservoir, Fushun , Fushun","extra":1,"x":5236,"g":["41.8864","124.0878"]}]/* 24 points -> 24 points */);

"""

soup = BeautifulSoup(html_doc, 'lxml')
script = soup.script.get_text()
map_search = re.search('mapInitWithData\((.*)\/\*.*', script)
mapData = map_search.group(1)
mapDataObj = json.loads(mapData)[0]
print mapDataObj["city"]
print mapDataObj["g"]
