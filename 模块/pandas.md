[toc]

## 目录
- 生成对象
- 查看数据
- 选择数据
- 操作数据

# 数据结构
    - 系列--series:一维标记均匀数组，大小不变
    
    - 数据帧--dataframe：二维标记，大小可变
    
    - 面板--panel：三维标记，大小可变
 
# 生成数据
- `pd.Series(list)`
- `pd.DataFrame(dir)`
# 查看数据
- 输出头尾
    - df.heal()
    - df.tail()
- 索引名/列名
    - df.index
    - df.columns
- 查看数据的统计摘要
    - df.describe()
- 分组
    - df.groupby()
- 求和
    - df.sum()  
- 均值
    - df.mean()
- 标准差
    - df.std() 
# 选择


# 操作 
- 行，列操作
    - pd.apply(function,*args,**args)
    - pd.apply(lambda)
- 设置为数字类型
    - pd.to_numeric()
- 重设索引
    - df.reset_index()
- se.value_counts()/pd.value_counts(array)
    - 对一维数组统计，返回系列，值为数量由大到小，索引为数组的值
    - 可用于提取出现频次最多的值
    ```
    dr
        0    爱情片
        1    爱情片
        2    爱情片
        3    动作片
    dr.value_counts()
        爱情片    3
        动作片    1
    dr.value_counts()index[0]
        爱情片
    ```
- u+-3*sign
# 输入输出
- df.read_csv(' ')
- df.to_csv(' ')