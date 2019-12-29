[toc]

# 数据结构
    - 系列--series:一维标记均匀数组，大小不变
    
    - 数据帧--dataframe：二维标记，大小可变
    
    - 面板--panel：三维标记，大小可变
 
## series
- 查看
    - df.index
    - df.columns
    - df.describe():查看数据的统计摘要
    - 求和
        - df.sum()  
    - 均值
        - df.mean()
    - 标准差
        - df.std() 
- 选择


- 操作 
    - 行，列操作
        - pd.apply(function,*args,**args)
        - pd.apply(lambda)
    - 设置为数字类型
        - pd.to_numeric()
    - 重设索引
        - df.reset_index()

- u+-3*sign
# 输入输出
- df.read_csv(' ')
- df.to_csv(' ')