# Python 绘图教程

本教程介绍如何使用 Python 读取 RMTDataPro 导出的数据并绘制专业图表。

## 📋 前提条件

安装必要的 Python 包：

```bash
pip install numpy matplotlib pandas
```

## 📂 数据读取

### 从 EDI 文件读取

```python
import numpy as np

def read_edi(filename):
    """读取 EDI 格式文件"""
    freq = []
    zxx_real = []
    zxx_imag = []
    zxy_real = []
    zxy_imag = []
    
    with open(filename, 'r') as f:
        in_mt_data = False
        for line in f:
            line = line.strip()
            
            if '>MT DATA' in line:
                in_mt_data = True
                continue
            
            if '>END' in line:
                in_mt_data = False
                continue
            
            if in_mt_data and line.startswith('>Z'):
                continue
            
            if in_mt_data:
                parts = line.split()
                if len(parts) >= 8:
                    freq.append(float(parts[0]))
                    zxx_real.append(float(parts[1]))
                    zxx_imag.append(float(parts[2]))
                    zxy_real.append(float(parts[3]))
                    zxy_imag.append(float(parts[4]))
    
    return np.array(freq), np.array(zxx_real), np.array(zxx_imag), \
           np.array(zxy_real), np.array(zxy_imag)
```

### 从 CSV 文件读取

```python
import pandas as pd

def read_csv(filename):
    """读取 CSV 格式数据"""
    df = pd.read_csv(filename)
    freq = df['Frequency'].values
    rho_xy = df['Rho_xy'].values
    phi_xy = df['Phase_xy'].values
    return freq, rho_xy, phi_xy
```

## 📊 基本 ρ-φ 曲线绘制

### 双 Y 轴曲线

```python
import matplotlib.pyplot as plt

def plot_rho_phi(freq, rho, phi):
    """绘制 ρ-φ 曲线"""
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    # 视电阻率曲线（左Y轴）
    color1 = 'tab:red'
    ax1.set_xlabel('Frequency (Hz)')
    ax1.set_ylabel('Apparent Resistivity (Ω·m)', color=color1)
    ax1.semilogx(freq, rho, color=color1, linewidth=2, marker='o', markersize=4)
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.grid(True, alpha=0.3)
    
    # 相位曲线（右Y轴）
    ax2 = ax1.twinx()
    color2 = 'tab:blue'
    ax2.set_ylabel('Phase (degrees)', color=color2)
    ax2.semilogx(freq, phi, color=color2, linewidth=2, marker='s', markersize=4)
    ax2.tick_params(axis='y', labelcolor=color2)
    
    plt.title('ρ-φ Curves')
    fig.tight_layout()
    plt.show()
```

## 📈 多测点叠加绘图

```python
def plot_multi_site(filenames, labels):
    """绘制多测点叠加曲线"""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
    
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    
    for i, (filename, label) in enumerate(zip(filenames, labels)):
        freq, rho, phi = read_edi(filename)
        color = colors[i % len(colors)]
        
        ax1.semilogx(freq, rho, color=color, linewidth=2, label=label)
        ax2.semilogx(freq, phi, color=color, linewidth=2, label=label)
    
    ax1.set_ylabel('Apparent Resistivity (Ω·m)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    ax2.set_xlabel('Frequency (Hz)')
    ax2.set_ylabel('Phase (degrees)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
```

## 🎨 专业样式设置

```python
plt.style.use('seaborn-v0_8-whitegrid')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 设置曲线样式
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['lines.markersize'] = 6
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['legend.fontsize'] = 10
```

## 💾 保存图片

```python
# 保存为 PNG
plt.savefig('rho_phi_curves.png', dpi=300, bbox_inches='tight')

# 保存为 PDF（矢量格式）
plt.savefig('rho_phi_curves.pdf', bbox_inches='tight')

# 保存为 SVG（可编辑矢量）
plt.savefig('rho_phi_curves.svg', bbox_inches='tight')
```

## 📚 完整示例

```python
#!/usr/bin/env python3
"""
RMTDataPro 数据绘图示例
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def main():
    # 数据目录
    data_dir = Path('./export_data')
    
    # 读取数据
    files = list(data_dir.glob('*.edi'))
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    colors = plt.cm.viridis(np.linspace(0, 1, len(files)))
    
    for i, f in enumerate(files):
        freq, rho, phi = read_edi(str(f))
        ax1.loglog(freq, rho, color=colors[i], label=f.stem)
        ax2.semilogx(freq, phi, color=colors[i], label=f.stem)
    
    ax1.set_ylabel('Apparent Resistivity (Ω·m)', fontsize=12)
    ax1.legend(loc='best')
    ax1.grid(True, alpha=0.3, which='both')
    
    ax2.set_xlabel('Frequency (Hz)', fontsize=12)
    ax2.set_ylabel('Phase (degrees)', fontsize=12)
    ax2.legend(loc='best')
    ax2.grid(True, alpha=0.3, which='both')
    
    plt.tight_layout()
    plt.savefig('multi_site_comparison.png', dpi=300)
    plt.show()

if __name__ == '__main__':
    main()
```

## 🔗 相关资源

- [Matplotlib 官方文档](https://matplotlib.org/stable/tutorials/index.html)
- [NumPy 文档](https://numpy.org/doc/stable/)
- [Pandas 文档](https://pandas.pydata.org/docs/)

---

**返回**: [实例展示](../gallery/index)
