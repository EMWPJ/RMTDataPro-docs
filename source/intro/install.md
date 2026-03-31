# 安装指南

本指南详细介绍 RMTDataPro 的系统要求与安装步骤。

## ⚙️ 系统要求

### 最低系统要求

| 项目 | 要求 |
|------|------|
| 操作系统 | Windows 10/11（64位） |
| 处理器 | Intel/AMD x64 处理器 |
| 内存 | 8GB RAM |
| 存储 | 2GB 可用磁盘空间 |
| 显卡 | 支持 OpenGL 3.3 |

### 推荐系统配置

| 项目 | 推荐配置 |
|------|----------|
| 操作系统 | Windows 11（64位） |
| 处理器 | Intel Core i5 / AMD Ryzen 5 及以上 |
| 内存 | 16GB RAM 及以上 |
| 存储 | SSD，5GB 可用空间 |

## 📦 依赖项

### 必需依赖

| 依赖 | 版本 | 说明 |
|------|------|------|
| Qt | 6.9+ | GUI 框架（msvc2022_64） |
| Intel oneAPI MKL | 2024.2+ | 数学库 |
| Visual Studio | 2022+ | C++ 编译器 |
| CMake | 3.16+ | 构建系统 |

### 可选依赖

| 依赖 | 版本 | 说明 |
|------|------|------|
| Intel oneAPI | 2024.2+ | 编译器（icx） |
| Ninja | - | 快速构建工具 |

## 🔧 构建步骤

### 1. 环境准备

确保已安装以下软件：

1. **Visual Studio 2022** (17.0+)
   - 下载地址: [Visual Studio Downloads](https://visualstudio.microsoft.com/downloads/)
   - 安装时选择 "使用 C++ 的桌面开发"

2. **Qt 6.9+**
   - 下载地址: [Qt Downloads](https://www.qt.io/download-qt-installer)
   - 安装组件: Qt 6.9.1 MSVC 2022 64-bit

3. **Intel oneAPI MKL 2024.2+**
   - 下载地址: [Intel oneAPI](https://www.intel.com/content/www/us/en/developer/tools/oneapi.html)
   - 组件: Intel oneAPI Base Toolkit

### 2. 获取源码

```bash
# 克隆仓库
git clone https://github.com/EMWPJ/EMDataPro.git

# 进入项目目录
cd EMDataPro
```

### 3. 使用 PowerShell 脚本构建

项目提供了便捷的构建脚本：

```powershell
# 配置项目（使用 MSVC，Release 模式）
.\config.ps1

# 使用 Intel 编译器配置
.\config.ps1 -Compiler intel

# 使用 Ninja 生成器
.\config.ps1 -Compiler msvc -Generator ninja

# 启用 OpenMP
.\config.ps1 -UseOpenMP

# 清理并重新配置
.\config.ps1 -Clean
```

### 4. 编译项目

```powershell
# 基本编译
.\build.ps1

# Debug 模式
.\build.ps1 -BuildType Debug

# 编译特定目标
.\build.ps1 -Target RMTDataPro

# 指定并行任务数
.\build.ps1 -Parallel 8

# 部署 Qt 依赖到输出目录
.\build.ps1 -Deploy
```

### 5. 运行程序

编译完成后，可执行文件位于：

```
build/msvc_release/bin/RMTDataPro/RMTDataPro.exe
```

运行程序：

```powershell
& "D:\code\EMDataPro\build\msvc_release\bin\RMTDataPro\RMTDataPro.exe"
```

## 📁 目录结构

构建后的目录结构：

```
build/msvc_release/
├── bin/
│   ├── RMTDataPro/          # RMTDataPro 可执行文件
│   │   └── RMTDataPro.exe
│   └── tests/               # 测试程序
├── lib/                     # 库文件
└── qmake/                   # Qt 项目文件
```

## ❓ 常见问题

### Q: 编译时报错 "Qt not found"

确保设置了 Qt 环境变量或使用 `-CMAKE_PREFIX_PATH` 指定 Qt 安装路径：

```powershell
.\config.ps1 -QtRoot "C:/Qt/6.9.1/msvc2022_64"
```

### Q: Intel MKL 链接错误

确保 Intel oneAPI 环境变量已正确设置：

```powershell
& "C:/Program Files (x86)/Intel/oneAPI/setvars.bat"
```

### Q: 缺少 vcruntime.dll

安装 Visual Studio 2022 Redistributable：
[Visual Studio Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist)

---

**下一节**: [快速开始](quickstart)
