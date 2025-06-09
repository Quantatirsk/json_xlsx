"""
json_xlsx 基本使用示例
"""

from json_xlsx import JsonToExcelConverter, convert_json_to_excel
from json_xlsx.examples import get_sample_data, get_sample_contracts


def example_1_simple_usage():
    """示例1: 简单用法"""
    print("=== 示例1: 简单用法 ===")
    
    # 简单的JSON数据
    data = [
        {
            "name": "张三",
            "age": 30,
            "address": {
                "city": "北京",
                "district": "海淀区"
            },
            "skills": ["Python", "JavaScript"]
        },
        {
            "name": "李四", 
            "age": 25,
            "address": {
                "city": "上海",
                "district": "浦东新区"
            },
            "skills": ["Java", "Spring"]
        }
    ]
    
    # 使用简化API
    result = convert_json_to_excel(data, "simple_example.xlsx")
    
    if result["success"]:
        print(f"✅ 转换成功！")
        print(f"   文件路径: {result['output_path']}")
        print(f"   记录数量: {result['records_count']}")
        print(f"   列数: {result['flattened_columns']}")
    else:
        print(f"❌ 转换失败: {result['error']}")


def example_2_advanced_usage():
    """示例2: 高级用法"""
    print("\n=== 示例2: 高级用法 ===")
    
    # 自定义配置
    custom_config = {
        "separator": "_",  # 使用下划线分隔符
        "max_depth": 10,   # 增加最大深度
        "max_column_width": 80,  # 调整最大列宽
    }
    
    # 创建转换器实例
    converter = JsonToExcelConverter(custom_config)
    
    # 获取示例数据
    data = get_sample_data()
    
    # 执行转换
    result = converter.convert(data, "advanced_example.xlsx")
    
    if result["success"]:
        print(f"✅ 转换成功！")
        print(f"   使用自定义配置")
        print(f"   分隔符: {custom_config['separator']}")
        print(f"   生成的列名示例: {result['column_names'][:5]}...")
    else:
        print(f"❌ 转换失败: {result['error']}")


def example_3_complex_data():
    """示例3: 复杂数据转换"""
    print("\n=== 示例3: 复杂数据转换 ===")
    
    # 获取复杂的合同数据
    contracts = get_sample_contracts()
    
    converter = JsonToExcelConverter()
    result = converter.convert_to_excel(contracts, "complex_contracts.xlsx")
    
    if result["success"]:
        print(f"✅ 复杂数据转换成功！")
        print(f"   处理了 {result['records_count']} 个合同")
        print(f"   生成了 {result['flattened_columns']} 个字段")
        print(f"   包含工作表: {', '.join(result['sheets'])}")
    else:
        print(f"❌ 转换失败: {result['error']}")


def example_4_single_object():
    """示例4: 单个对象转换"""
    print("\n=== 示例4: 单个对象转换 ===")
    
    # 单个对象
    single_object = {
        "product": "笔记本电脑",
        "price": 8999.99,
        "specs": {
            "cpu": "Intel i7",
            "memory": "16GB",
            "storage": "512GB SSD"
        },
        "features": ["轻薄", "长续航", "高性能"],
        "available": True
    }
    
    # 直接转换单个对象
    result = convert_json_to_excel(single_object, "single_product.xlsx")
    
    if result["success"]:
        print(f"✅ 单个对象转换成功！")
        print(f"   扁平化后有 {result['flattened_columns']} 个字段")
    else:
        print(f"❌ 转换失败: {result['error']}")


def example_5_error_handling():
    """示例5: 错误处理"""
    print("\n=== 示例5: 错误处理 ===")
    
    # 空数据测试
    result = convert_json_to_excel([], "empty_data.xlsx")
    print(f"空数据处理: {'成功' if result['success'] else '失败 - ' + result['error']}")
    
    # 无效路径测试  
    result = convert_json_to_excel([{"test": "data"}], "/invalid/path/test.xlsx")
    print(f"无效路径处理: {'成功' if result['success'] else '失败 - ' + result['error']}")


def main():
    """运行所有示例"""
    print("🚀 json_xlsx 使用示例")
    print("=" * 50)
    
    try:
        example_1_simple_usage()
        example_2_advanced_usage()
        example_3_complex_data()
        example_4_single_object()
        example_5_error_handling()
        
        print("\n" + "=" * 50)
        print("🎉 所有示例运行完成！")
        print("📁 生成的文件:")
        print("   - simple_example.xlsx")
        print("   - advanced_example.xlsx") 
        print("   - complex_contracts.xlsx")
        print("   - single_product.xlsx")
        
    except Exception as e:
        print(f"❌ 运行示例时出错: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()