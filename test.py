"""
测试json_xlsx库
"""

import requests
from json_xlsx import convert_json_to_excel

# 获取响应数据
response = requests.get("https://dummyjson.com/recipes", timeout=10)
response_data = response.json()

# 获取第一个key的值
json_data = response_data.get(list(response_data.keys())[0])

# 配置表头背景色和字体颜色
CONFIG = {"header_background_color": "FFFFFF", "header_font_color": "000000"}

# 输出路径
OUTPUT_PATH = "sample.xlsx" 

# 转换数据
result = convert_json_to_excel(json_data, OUTPUT_PATH, CONFIG)

# 打印输出路径
print(result["output_path"])
