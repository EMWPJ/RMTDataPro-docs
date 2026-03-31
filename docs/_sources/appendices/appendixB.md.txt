# 附录 B：文件格式

本附录详细介绍 RMTDataPro 支持的文件格式。

## 📂 工程文件

### .rmtproj（工程文件）

RMTDataPro 工程文件格式，基于 JSON 存储。

**文件结构**:

```json
{
    "version": "0.1.0",
    "projectName": "示例工程",
    "created": "2026-03-30T10:00:00",
    "modified": "2026-03-30T15:30:00",
    "lines": [
        {
            "name": "测线1",
            "sites": [
                {
                    "name": "S001",
                    "sbffiles": ["path/to/file1.sbf"],
                    "processed": true
                }
            ]
        }
    ],
    "fftParamFile": "default_fft.json"
}
```

## 📊 数据文件

### SBF（Station Binary Format）

RMT 测站二进制数据格式。

**文件结构**:

| 段类型 | 说明 | 大小（典型） |
|--------|------|--------------|
| Header | 文件头 | 64 bytes |
| Text | 文本信息 | 可变 |
| Ini | 初始化参数 | 可变 |
| Trass | 时间序列 | 可变 |
| Spectrum | 频谱数据 | 可变 |
| Device Parameter | 设备参数 | 可变 |
| Registrar Parameter | 注册参数 | 可变 |
| CheckSum | 校验和 | 4 bytes |

### EDI（Electrical Data Interchange）

MT 数据标准交换格式。

**文件示例**:

```text
>=HEAD
  FILENAME="station001.edi"
  ACQBY="Operator"
  DATE="2026-03-30"
  PROJ="RMT Survey"
  LOC="Study Area"
  LAT=40.0
  LON=120.0
  ELEV=100.0
  SIGNAL="RMT"
  UNITS="SI"
>MT DATA
>Z rot=0
  100.0  45.2  -15.3  72.1  12.3  -85.2  35.6  158.4
  200.0  48.5  -12.8  68.4  15.1  -82.1  38.2  155.3
>END
```

**数据说明**:

| 列 | 内容 |
|----|------|
| 1 | 频率 (Hz) |
| 2-3 | Zxx (实部, 虚部) |
| 4-5 | Zxy (实部, 虚部) |
| 6-7 | Zyx (实部, 虚部) |
| 8-9 | Zyy (实部, 虚部) |

### CSV（逗号分隔值）

文本表格格式，便于 Excel 等软件处理。

**文件格式**:

```text
Frequency,Rho_xx,Phi_xx,Rho_xy,Phi_xy,Rho_yx,Phi_yx,Rho_yy,Phi_yy
100.0,10.5,-15.3,45.2,72.1,12.3,-85.2,35.6,158.4
200.0,12.3,-12.8,48.5,68.4,15.1,-82.1,38.2,155.3
```

### TXT（文本格式）

每行一条记录，空格分隔。

**文件格式**:

```
频率(Hz)  ρxx(Ω·m)  φxx(°)  ρxy(Ω·m)  φxy(°)  ρyx(Ω·m)  φyx(°)  ρyy(Ω·m)  φyy(°)
100.0     10.5      -15.3    45.2       72.1     12.3       -85.2    35.6       158.4
200.0     12.3      -12.8    48.5       68.4     15.1       -82.1    38.2       155.3
```

## ⚙️ 配置文件

### FFT 参数文件 (.json)

```json
{
    "windowLength": 512,
    "overlap": 0.5,
    "windowMode": "Multiple",
    "timeBandwidthProduct": 2.0,
    "numWindows": 3,
    "bandwidth": 3,
    "impedanceType": "Tensor",
    "averageType": "WeightedMean",
    "targetFrequencies": {
        "39000.0": [100, 200, 500, 1000],
        "312000.0": [5000, 10000, 20000]
    }
}
```

### 校准文件 (.cal)

二进制或文本格式，包含系统响应校准数据。

## 📦 导出目录结构

批量导出时，自动创建以下目录结构：

```
输出目录/
├── 测线1/
│   ├── S001.edi
│   ├── S001.csv
│   ├── S002.edi
│   └── S002.csv
├── 测线2/
│   ├── S003.edi
│   └── S003.csv
└── export_log.txt
```

---

**返回**: [附录索引](../index)
