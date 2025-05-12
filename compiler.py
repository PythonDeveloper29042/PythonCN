"""
@author: PythonDeveloper29042
@date:
@name: compiler.py
@description: A simple compiler for PythonCN
"""

from os import system

# 将英文内置名称替换为中文内置名称 Replace English built-in names with Chinese built-in names
builtins = {
    "输出": "print",
    "输入": "input",
    "范围": "range",
    "类型": "type",
    "长度": "len",
    "整数": "int",
    "浮点数": "float",
    "字符串": "str",
    "列表": "list",
    "元组": "tuple",
    "字典": "dict",
    "集合": "set",
}

# 将英文关键字替换为中文关键字 Replace English keywords with Chinese keywords
keywords = {
    "如果": "if",
    "否则": "else",
    "循环": "for",
    "在": "in",
    "范围": "range",
    "打印": "print",
    "输入": "input",
    "返回": "return",
    "函数": "def",
    "类": "class",
    "导入": "import",
    "从": "from",
    "是": "True",
    "否": "False",
    "循环当": "while",
    "继续": "continue",
    "跳出": "break",
    "尝试": "try",
    "异常": "except",
    "最终": "finally",
    "抛出": "raise",
    "全局": "global",
    "非": "not",
    "与": "and",
    "或": "or",
    "是": "is",
}

# 将半角字符替换为全角字符，以方便中文输入 Replace half-width symbols with full-width symbols
symbols = {
    "　": " ",
    "，": ",",
    "。": ".",
    "；": ";",
    "：": ":",
    "！": "!",
    "（": "(",
    "）": ")",
    # "【": "[",
    # "】": "]",
    "、": "\\",
    "“": "\"",
    "”": "\"",
    "‘": "'",
    "’": "'",
    # "《": "<",
    # "》": ">",
    "＂": "\"",
    "＇": "'",
    "．": ".",
    "＜": "<",
    "＞": ">",
    "＃": "#",
    "％": "%",
    "＋": "+",
    "－": "-",
    "／": "/",
    "＝": "=",
    "＊": "*",
    "１": "1",
    "２": "2",
    "３": "3",
    "４": "4",
    "５": "5",
    "６": "6",
    "７": "7",
    "８": "8",
    "９": "9",
    "０": "0"
}

dic = {**builtins, **keywords, **symbols}

def translate_code(code: str) -> str:
    """
    将PythonCN代码翻译为Python代码
    Translate PythonCN code to Python code.
    Args:
        code (str): 要翻译的代码 The code to be translated.
    Returns:
        str: 翻译后的代码 The translated code.
    """
    for key, value in dic.items():
        code = code.replace(key, value)
    return code

def compile_code(code: str) -> None:
    """
    编译PythonCN代码
    Compile PythonCN code.
    Args:
        code (str): 要编译的代码 The code to be compiled.
    Returns:
        None
    """
    # 将代码翻译为Python代码 Translate the code to Python code.
    python_code = translate_code(code)
    # 将翻译后的代码写入文件 Write the translated code to a file.
    with open("temp.py", "w", encoding="utf-8") as f:
        f.write(python_code)
    # 执行编译后的代码 Execute the compiled code.
    system("python temp.py")

def main():
    filename = input("请输入要编译的文件名 (文件名.pycn): ")
    # 如果找不到文件，则提示并退出程序 If the file is not found, prompt and exit the program.
    if not filename:
        print(f"找不到文件 {filename} ，请检查文件名和路径。")
        return
    # 如果找到文件了 If the file is found
    else:
        # 读取文件并编译 Read the file and compile it.
        with open(filename, "r", encoding="utf-8") as f:
            code = f.read()
        compile_code(code)

if __name__ == "__main__":
    main()