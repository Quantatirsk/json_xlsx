#!/usr/bin/env python3
"""
运行json_xlsx库的测试和示例
"""

import sys
import os
from pathlib import Path

# 添加当前目录到Python路径
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

def run_basic_test():
    """运行基本功能测试"""
    print("🧪 运行基本功能测试...")
    print("=" * 50)
    
    try:
        # 导入并测试基本功能
        from json_xlsx import convert_json_to_excel, JsonToExcelConverter
        from json_xlsx.examples import get_sample_data
        
        # 测试数据
        test_data = [
            {
                "name": "测试用户",
                "age": 30,
                "info": {
                    "city": "北京",
                    "skills": ["Python", "Excel"]
                }
            }
        ]
        
        print("✅ 导入成功")
        
        # 测试简化API
        result = convert_json_to_excel(test_data, "test_output.xlsx")
        
        if result["success"]:
            print("✅ 简化API测试成功")
            print(f"   生成列数: {result['flattened_columns']}")
        else:
            print(f"❌ 简化API测试失败: {result['error']}")
            return False
            
        # 测试转换器类
        converter = JsonToExcelConverter()
        result2 = converter.convert(test_data, "test_output2.xlsx", verbose=False)
        
        if result2["success"]:
            print("✅ 转换器类测试成功")
        else:
            print(f"❌ 转换器类测试失败: {result2['error']}")
            return False
            
        # 测试示例数据
        sample_data = get_sample_data()
        result3 = convert_json_to_excel(sample_data, "sample_data.xlsx")
        
        if result3["success"]:
            print("✅ 示例数据测试成功")
            print(f"   处理记录数: {result3['records_count']}")
        else:
            print(f"❌ 示例数据测试失败: {result3['error']}")
            return False
            
        print("\n🎉 所有基本测试通过！")
        return True
        
    except Exception as e:
        print(f"❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def run_unit_tests():
    """运行单元测试"""
    print("\n🔬 运行单元测试...")
    print("=" * 50)
    
    try:
        # 尝试运行pytest
        import subprocess
        result = subprocess.run([
            sys.executable, "-m", "pytest", "tests/", "-v"
        ], capture_output=True, text=True, cwd=current_dir)
        
        print(result.stdout)
        if result.stderr:
            print("错误输出:")
            print(result.stderr)
            
        if result.returncode == 0:
            print("✅ 单元测试全部通过")
            return True
        else:
            print("❌ 部分单元测试失败")
            return False
            
    except ImportError:
        print("⚠️  未安装pytest，跳过单元测试")
        return True
    except Exception as e:
        print(f"❌ 运行单元测试时出错: {e}")
        return False


def run_examples():
    """运行示例代码"""
    print("\n📝 运行示例代码...")
    print("=" * 50)
    
    try:
        # 导入并运行示例
        examples_file = current_dir / "examples" / "basic_usage.py"
        if examples_file.exists():
            import importlib.util
            spec = importlib.util.spec_from_file_location("basic_usage", examples_file)
            examples_module = importlib.util.module_from_spec(spec)
            
            # 重定向到当前目录执行
            old_cwd = os.getcwd()
            os.chdir(current_dir)
            
            try:
                spec.loader.exec_module(examples_module)
                print("✅ 示例代码运行成功")
                return True
            finally:
                os.chdir(old_cwd)
        else:
            print("⚠️  找不到示例文件")
            return False
            
    except Exception as e:
        print(f"❌ 运行示例时出错: {e}")
        import traceback
        traceback.print_exc()
        return False


def check_dependencies():
    """检查依赖包"""
    print("📦 检查依赖包...")
    print("=" * 50)
    
    dependencies = ["pandas", "openpyxl"]
    all_good = True
    
    for dep in dependencies:
        try:
            __import__(dep)
            print(f"✅ {dep} - 已安装")
        except ImportError:
            print(f"❌ {dep} - 未安装")
            all_good = False
    
    if not all_good:
        print("\n请安装缺失的依赖包:")
        print("pip install pandas openpyxl")
        
    return all_good


def cleanup_test_files():
    """清理测试文件"""
    print("\n🧹 清理测试文件...")
    
    test_files = [
        "test_output.xlsx",
        "test_output2.xlsx", 
        "sample_data.xlsx",
        "simple_example.xlsx",
        "advanced_example.xlsx",
        "complex_contracts.xlsx",
        "single_product.xlsx"
    ]
    
    cleaned = 0
    for file in test_files:
        file_path = current_dir / file
        if file_path.exists():
            try:
                file_path.unlink()
                cleaned += 1
            except Exception as e:
                print(f"⚠️  无法删除 {file}: {e}")
    
    if cleaned > 0:
        print(f"🗑️  清理了 {cleaned} 个测试文件")


def main():
    """主函数"""
    print("🚀 json_xlsx 库测试套件")
    print("=" * 50)
    
    # 检查依赖
    if not check_dependencies():
        print("\n❌ 依赖检查失败，请先安装必要的依赖包")
        return 1
    
    # 运行测试
    tests_passed = 0
    total_tests = 3
    
    if run_basic_test():
        tests_passed += 1
        
    if run_unit_tests():
        tests_passed += 1
        
    if run_examples():
        tests_passed += 1
    
    # 清理测试文件
    cleanup_test_files()
    
    # 总结
    print("\n" + "=" * 50)
    print(f"📊 测试结果: {tests_passed}/{total_tests} 通过")
    
    if tests_passed == total_tests:
        print("🎉 所有测试都通过了！json_xlsx库运行正常")
        return 0
    else:
        print("⚠️  部分测试失败，请检查上面的错误信息")
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)