"""
测试json_xlsx库
"""

import requests
from json_xlsx import convert_json_to_excel, merge_sheets

# 获取响应数据
response = requests.get("https://dummyjson.com/recipes", timeout=10)
response_data = response.json()

# 获取第一组数据
JSON_DATA_1 = response_data.get(list(response_data.keys())[0])

# 获取第二组数据
JSON_DATA_2 = [
    {
        "合同编号": "CONTRACT-2025-IT-001",
        "合同名称": "企业数字化转型系统开发项目",
        "合同类型": "技术开发合同",
        "签署日期": "2025-06-01",
        "生效日期": "2025-06-15",
        "到期日期": "2026-12-31",
        "合同状态": "执行中",
        "合同金额": {
            "总金额": 2800000.00,
            "币种": "人民币",
            "税率": 0.06,
            "税额": 168000.00,
            "含税总额": 2968000.00,
        },
        "特殊条款": {
            "创新激励": "达成关键里程碑可获得额外奖金",
            "绩效指标": ["系统可用性>99.9%", "用户满意度>95%"],
        },
    },
    {
        "合同编号": "CONTRACT-2025-PR-002",
        "合同名称": "办公设备及IT硬件采购合同",
        "合同类型": "采购合同",
        "签署日期": "2025-06-05",
        "生效日期": "2025-06-10",
        "到期日期": "2025-12-31",
        "合同状态": "执行中",
        "合同金额": {
            "总金额": 1560000.00,
            "币种": "人民币",
            "税率": 0.13,
            "税额": 202800.00,
            "含税总额": 1762800.00,
        },
        "环保要求": {
            "节能等级": "能源之星认证",
            "碳排放补偿": "每批设备捐赠碳信用",
            "回收承诺": "提供免费设备回收服务",
        },
    },
    {
        "合同编号": "CONTRACT-2025-CO-003",
        "合同名称": "云计算服务框架协议",
        "合同类型": "服务合同",
        "签署日期": "2025-07-15",
        "生效日期": "2025-08-01",
        "到期日期": "2026-07-31",
        "合同状态": "待执行",
        "合同金额": {
            "总金额": 3600000.00,
            "币种": "人民币",
            "税率": 0.09,
            "税额": 324000.00,
            "含税总额": 3924000.00,
        },
        "SLA性能指标": {
            "可用性保证": "99.99%",
            "响应时间要求": "平均<50毫秒",
            "赔偿机制": "未达标扣除当月服务费20%",
        },
    },
    {
        "合同编号": "CONTRACT-2025-RE-004",
        "合同名称": "研发协作与技术许可协议",
        "合同类型": "技术许可",
        "签署日期": "2025-05-20",
        "生效日期": "2025-06-01",
        "到期日期": "2027-05-31",
        "合同状态": "审核中",
        "合同金额": {
            "总金额": 1200000.00,
            "币种": "人民币",
            "税率": 0.06,
            "税额": 72000.00,
            "含税总额": 1272000.00,
        },
        "知识产权条款": {
            "专利共享": "联合申请专利",
            "royalty比例": "销售额的5-8%",
            "技术保密": "严格保密协议",
            "使用范围": "全球范围内非独占许可",
        },
    },
]

# 形成多组数据
JSON_DATA = [JSON_DATA_1, JSON_DATA_2]

# 输出路径
TEMPLATE_NAME_1 = "RECIPE"
TEMPLATE_NAME_2 = "CONTRACT"

TEMPLATE_NAME = [TEMPLATE_NAME_1, TEMPLATE_NAME_2]

# 配置表头背景色和字体颜色
CONFIG_1 = {
    "processed_sheet_name": TEMPLATE_NAME_1,
}
CONFIG_2 = {
    "processed_sheet_name": TEMPLATE_NAME_2,
}
CONFIG = [CONFIG_1, CONFIG_2]

MERGE_SHEETS_NAME = "MERGED.xlsx"

# 转换数据
for i, item in enumerate(JSON_DATA):
    result = convert_json_to_excel(item, f"{TEMPLATE_NAME[i]}.xlsx", CONFIG[i])  # index从0开始，文件名从1开始
    # 打印输出路径
    print(result["output_path"])

# 合并数据
merge_sheets([f"{TEMPLATE_NAME[i]}.xlsx" for i in range(len(JSON_DATA))], MERGE_SHEETS_NAME)  # 合并时index从1开始
