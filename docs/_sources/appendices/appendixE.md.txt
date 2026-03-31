# 附录 E：故障排除

本附录提供 RMTDataPro 故障诊断和解决方法。

## 🔍 诊断流程

遇到问题时，请按以下步骤诊断：

```mermaid
    graph TB
        A[出现问题] --> B{错误类型}
        B --> |启动失败| C[检查运行库]
        B --> |运行错误| D[查看日志]
        B --> |数据问题| E[检查数据文件]
        B --> |导出失败| F[检查权限/空间]
        
        C --> G{问题解决?}
        D --> G
        E --> G
        F --> G
        
        G --> |是| H[完成]
        G --> |否| I[联系支持]
```

## 📋 常见错误与解决

### 错误 1: "无法加载 Qt 平台插件"

```
Could not load Qt platform plugin "windows"
```

**解决方法**:

1. 部署 Qt 依赖：
   ```powershell
   .\build.ps1 -Deploy
   ```

2. 或手动复制 Qt 插件目录：
   ```
   build/bin/RMTDataPro/plugins/
   ```

### 错误 2: "找不到 Intel MKL 函数"

```
The procedure entry point mkl_?fft could not be located...
```

**解决方法**:

1. 设置 Intel MKL 环境变量：
   ```powershell
   & "C:/Program Files (x86)/Intel/oneAPI/setvars.bat"
   ```

2. 或将 MKL DLL 复制到可执行文件目录

### 错误 3: "内存不足"

```
Failed to allocate 2048 MB of memory
```

**解决方法**:

1. 减少 FFT 窗口长度
2. 减少同时处理的测点数量
3. 增加系统虚拟内存

### 错误 4: "SBF 文件校验失败"

```
SBF file checksum validation failed
```

**解决方法**:

1. 重新下载或复制 SBF 文件
2. 联系数据提供方确认文件完整性

## 📊 日志文件

### 日志位置

| 环境 | 日志路径 |
|------|----------|
| Windows | `%APPDATA%/RMTDataPro/logs/` |
| Linux | `~/.local/share/RMTDataPro/logs/` |

### 日志级别

| 级别 | 内容 |
|------|------|
| ERROR | 错误信息 |
| WARNING | 警告信息 |
| INFO | 一般信息 |
| DEBUG | 调试信息 |

### 启用详细日志

在 FFT 参数设置中启用"详细日志"选项。

## 🧪 测试工具

### 内置测试程序

编译后包含测试程序，位于：

```
build/msvc_release/bin/tests/
```

| 测试程序 | 功能 |
|----------|------|
| `test_fft_processor.exe` | FFT 处理器测试 |
| `test_powerline_filter.exe` | 工频滤波器测试 |

### 运行测试

```powershell
# 运行 FFT 处理器测试
.\build\msvc_release\bin\tests\test_fft_processor.exe

# 运行工频滤波器测试
.\build\msvc_release\bin\tests\test_powerline_filter.exe
```

## 📞 技术支持

如问题无法解决，请提供：

1. 软件版本号（关于对话框）
2. 错误日志文件
3. 复现步骤描述
4. 系统环境信息

---

**返回**: [附录索引](../index)
