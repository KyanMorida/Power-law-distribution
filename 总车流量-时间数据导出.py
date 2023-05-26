import os
import traci
import matplotlib.pyplot as plt

# 设置SUMO仿真配置文件路径
config_path = os.path.join(r'D:\SOFTWARE\SUMO\tools\2023-05-24-18-55-34', 'osm.sumocfg')

# 启动SUMO仿真
traci.start(['sumo-gui', '-c', config_path])

# 获取仿真时间步长
time_step = traci.simulation.getDeltaT()

# 存储时间和总车辆数的列表
time_list = []
vehicle_count_list = []

# 迭代仿真步数
while traci.simulation.getMinExpectedNumber() > 0:
    # 获取当前仿真时间
    simulation_time = traci.simulation.getTime()

    # 获取当前网络中的车辆ID列表
    vehicle_ids = traci.vehicle.getIDList()

    # 获取当前网络中的总车辆数
    vehicle_count = len(vehicle_ids)

    # 将时间和总车辆数添加到列表中
    time_list.append(simulation_time)
    vehicle_count_list.append(vehicle_count)

    # 运行下一个仿真步
    traci.simulationStep()

# 关闭SUMO仿真
traci.close()

# 绘制车辆流量随时间变化的图表
plt.plot(time_list, vehicle_count_list)
plt.xlabel('Simulation Time')
plt.ylabel('Total Vehicle Count')
plt.title('Total Vehicle Count over Time')
plt.grid(True)
plt.show()
