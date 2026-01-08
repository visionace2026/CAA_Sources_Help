# -*- coding: utf-8 -*-
"""
全局配置
"""

# 应用信息
APP_NAME = "CATIA CAA源码框架快速生成器"
APP_VERSION = "2.0"

# 窗口尺寸
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500

# 树形区域尺寸
TREE_WIDTH = 250
TREE_HEIGHT = 420

# 常用第三方库列表
THIRD_PARTY_LIBS = [
    ("OpenSSL", "加密库"),
    ("RapidJSON", "JSON解析"),
    ("TinyXML2", "XML解析"),
    ("SQLite", "轻量数据库"),
    ("cURL", "网络请求"),
    ("Eigen", "矩阵运算"),
    ("Boost", "C++扩展库"),
    ("spdlog", "日志库"),
    ("fmt", "格式化库"),
]

# CAA标准目录
CAA_FRAMEWORK_DIRS = [
    "PublicInterfaces",
    "LocalInterfaces",
    "PrivateInterfaces",
]

# 快速模板定义
QUICK_TEMPLATES = {
    "crud": {
        "name": "CRUD命令组",
        "commands": ["CreateCmd", "ReadCmd", "UpdateCmd", "DeleteCmd"],
        "dialogs": ["CreateDlg", "EditDlg"],
        "classes": [],
    },
    "viewer": {
        "name": "Viewer命令组",
        "commands": ["ZoomInCmd", "ZoomOutCmd", "PanCmd", "RotateCmd", "FitAllCmd"],
        "dialogs": [],
        "classes": [],
    },
    "selection": {
        "name": "Selection命令",
        "commands": ["SelectionCmd"],
        "dialogs": ["SelectionDlg"],
        "classes": ["SelectionFilter"],
    },
}
