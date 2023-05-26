import os
import traci
import matplotlib.pyplot as plt
import numpy as np
# 设置SUMO仿真配置文件路径
config_path = os.path.join(r'D:\SOFTWARE\SUMO\tools\2023-05-24-18-55-34', 'osm.sumocfg')

# 启动SUMO仿真
traci.start(['sumo-gui', '-c', config_path])

# 获取仿真时间步长
time_step = traci.simulation.getDeltaT()

# 定义目标边（edge）的ID
edge_id = '1102154066#0'  # 替换为您要专注的边ID

# 存储边车流量的变化
edge_vehicle_count = []

# 迭代仿真步数
while traci.simulation.getMinExpectedNumber() > 0:
    # 运行下一个仿真步
    traci.simulationStep()

    # 获取当前仿真时间
    simulation_time = traci.simulation.getTime()

    # 获取边上的车辆ID列表
    vehicle_ids = traci.edge.getLastStepVehicleIDs(edge_id)

    # 计算边上的车辆数
    vehicle_count = len(vehicle_ids)

    # 将时间和边车流量添加到列表中
    edge_vehicle_count.append((simulation_time, vehicle_count))

# 关闭SUMO仿真
traci.close()

# 提取时间和车流量数据
times = [time for time, _ in edge_vehicle_count]
vehicle_counts = [count for _, count in edge_vehicle_count]

print('total vehicle counts: ',np.array(vehicle_counts).sum())
# 绘制车流量随时间变化的曲线
plt.plot(times, vehicle_counts)
plt.xlabel('Time')
plt.ylabel('Vehicle Count')
plt.title('Vehicle Count Variation for Edge')
plt.grid(True)
plt.show()



