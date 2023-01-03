import matplotlib.pyplot as plt
import pandas as pd
import os, sys

# dirpath='.\\' # PY执行
dirpath=os.path.realpath(os.path.dirname(sys.executable)) # EXE执行
print(dirpath)
# floderpath, flodername=[], []
# filepath=[]
baro={'filepath':[], 'flodername':[]}

if __name__ == "__main__":


    # 获取需要处理数据的气压原始文件路径及子文件夹名称
    for i in os.listdir(dirpath):
        path = os.path.join(dirpath,i)
        if os.path.isdir(path):
            baro['filepath'].append(os.path.join(path,os.listdir(path)[0]))    
            baro['flodername'].append(i)
    # print(filepath,flodername)

    # 绘图
    for i in range(len(baro['filepath'])):
        # print(baro['filepath'][i],baro['flodername'][i])
        df = pd.read_csv(baro['filepath'][i], header=9)
        # plt.clf()
        x=range(0,len(df))
        plt.plot(x,df['pressure'],label=baro['flodername'][i])
        plt.legend(loc="best", borderaxespad=0)
    plt.show()

    pass