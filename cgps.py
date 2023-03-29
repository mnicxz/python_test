import pandas as pd
from pathlib import Path
import os, sys
from typing import Union, Optional
from datetime import datetime
from units.io import gtx2csv

# 读取文件
def read_raw_data(
    fpath: Union[str, Path],
    pattern_session: str,
    pattern_dut: str,
    pattern_gt: str,
) -> dict:
    """
    @param fpath: 原始文件路径
    @param session_path: 同一时间所有原始文件路径
    @param dut_path: dut原始文件路径
    @param gt_path: gt原始文件路径
    @return: 
    """
    session = {}

    dut = {'label': 'dut'}
    duts_path = list(fpath.glob(pattern_dut))
    for dut_path in duts_path:
        try:
            df = gtx2csv.gpx2csv(dut_path)
        except pd.errors.EmptyDataError:
            df = pd.DataFrame.from_dict({})
        # df['timestamps'] = datetime.strptime( df['time'], '%Y/%m/%d %H:%M:%S+00')
        datetime_index = pd.to_datetime(df['Time'])
        timestamp = datetime_index.astype('int64') // 10**9
        df['timestamp'] = timestamp -28800
        # df.set_index
        # df = df.loc[:, ['Lat','Lon','time','timestamp']]

        dut['path'] = dut_path
        dut['data'] = df
        session['dut'] = dut
    
    gt = {'label': 'gt'}
    gts_path = list(fpath.glob(pattern_gt))
    for gt_path in gts_path:
        try:
            df = pd.read_csv(gt_path, header=1)
        except pd.errors.EmptyDataError:
            df = pd.DataFrame.from_dict({})
        df['timestamp'] = df['EventTimestamp(ms)'] / 1000
        gt['path'] = gt_path
        gt['data'] = df
        session['gt'] = gt

    # 同步文件
    session['dut']['data'].set_index('timestamp', inplace=True)
    session['gt']['data'].set_index('timestamp', inplace=True)

    merged_df = pd.merge(session['gt']['data'], session['dut']['data'], on='timestamp', how='outer')

    # 计算距离
    # try:
    merged_df['Distance'] = merged_df.apply(lambda row: gtx2csv.getDistance(row['Lat'], row['Lon'], row['Latitude'], row['Longitude']), axis=1)
    # except:
        # print("计算距离失败")
    return merged_df


if __name__ == "__main__":
    print(
        """
        将金标数据和设备数据对齐时间戳，计算同一时间两个点的距离
        金标数据文件和设备数据文件需放置在该脚本文件夹下
        结果文件会同步输出导该文件下
        """
    )
    # fpath=Path('.\\')
    fpath=Path(os.path.realpath(os.path.dirname(sys.executable))) # EXE执行
    output=True

    session_path='[A-Za-z0-9]'
    dut_path='*-GPX.gpx'
    gt_path='*-location.csv'

    raw_data = read_raw_data(fpath,session_path,dut_path,gt_path)
    # print(list(fpath.glob('DUT_*')))

    if output:
        raw_data.to_excel(str(fpath/'result.xlsx'))
    pass