'''
    pip是Python的包管理工具，该工具提供了对Python包的查找、下载、安装、卸载功能

'''
import matplotlib.pyplot as plt 
import numpy as np 
x=np.linspace(0,20,100,endpoint=True)
plt.plot(x,np.sin(x))
plt.show()
print("hello world")