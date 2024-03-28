import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from mpl_toolkits.mplot3d import Axes3D

# 读取Excel文件(注意检查路径：反斜杠-->正斜杠)
data = pd.read_csv('E:/丽院/其他项/发刊/云图1.csv')

# 创建地图
fig = plt.figure(figsize=(10, 6))
# ax = plt.axes(projection=ccrs.PlateCarree())
ax = fig.add_subplot(111, projection='3d')

# 绘制海岸线、国界线等 (2D)
# ax.coastlines()
# ax.add_feature(cfeature.BORDERS, linestyle=':')
# ax.add_feature(cfeature.STATES, linestyle='--')

# 根据时间点分组
time_groups = data.groupby('time')

# 绘制数据点
for time, group in time_groups:
    sc = ax.scatter(group['lon'], group['lat'], group['time'], c = group['co2'], cmap='viridis', s=100, alpha=0.7)

# 添加色标
cbar = plt.colorbar(sc, shrink=0.5)
cbar.set_label('CO2 Concentration')

# 添加标题和标签
ax.set_title('CO2 Concentration Map')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_zlabel('Time')

plt.title('3D CO2 Concentration Map')

#保存图片
# plt.savefig('导出云图2.png', dpi=300, bbox_inches='tight')



# 显示图形
plt.show()
