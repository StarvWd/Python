[toc]

# ndarray的创建

- 从列表等其他Python的结构进行转换
	
	- `a = np.array([1,2,3],[4,5,6])`
	
	  > [[1 2 3]  
	    [4 5 6]]
- 使用特殊的库函数
    - `a = np.random.rand((2,2))`

      > [[0.64970951 0.2861271 ]  
        [0.96183084 0.87542968]]
- 使用Numpy内部功能函数
    - `a = np.zeros((3,4))`
      
         > [[0. 0. 0.]  
            [0. 0. 0.]]
         
    - `c = np.ones((3,4))`
      
       > [[1. 1. 1.]  
       > [1. 1. 1.]]
       
    - `a = np.empty((2,3))`
      
      > [[0.00000000e+000 8.99166274e-315 6.91691904e-323]  
      > [            nan 3.22444304e-086 2.98151668e+284]]
      
    - `a = np.full((2,3),1)`
      
      > [[1 1 1]  
      > [1 1 1]]
      
    - `a = np.eye(3,3)`
      
      > [[1. 0. 0.]  
      > [0. 1. 0.]  
      > [0. 0. 1.]]
      
    - `a = np.arange(1,3,0.5)`：等差数列，左闭右开，0.5表示步长
      
        > [1.  1.5 2.  2.5]
        
    - `b = np.linspace(1,5,5)`：等差数列，左闭右闭，5表示个数
      
        > [1. 2. 3. 4. 5.]
        
    - `c = np.logspace(0,2,5)`：等比数列，左闭右闭，10^0,10^2, 5表示个数
      
        > [ 1.   3.16  10.   31.62   100. ]
        
# ndarray的访问
- 类似列表，可使用切片，与列表不同，与原数组共享空间；使用整数序列，不与原数组共享空间

    ```python
    import numpy as np
    x = np.arange(10)
    a = x[1:5]
    b = x[[0,-1,5]]
    print(a.base is x)
    print(b.base is x)
    print(x)
    print(a)
    print(b)
    ```

    > True  
    > False  
    > [0 1 2 3 4 5 6 7 8 9]  
    > [1 2 3 4]  
    > [0 9 5]

- 布尔索引，不适用布尔列表

    ```python
    import numpy as np
    x = np.random.rand(6)
    print(x)
    print(x > 0.5)
    print(x[x>0.5])
    ```

    > [0.57642904 0.58257329 0.33999225 0.84596796 0.39968613 0.67034443]  
    > [ True  True False  True False  True]  
    > [0.57642904 0.58257329 0.84596796 0.67034443]  

- 多维数组的访问,下标在同一个[  ,  ]中用 逗号 隔开

    ```python
    import numpy as np
    x = np.array([[1,2,3],[4,5,6],[7,8,9]])
    print(x[2,[1,0]])
    print(x[0:2,::-1])
    ```
    
    > [8 7]  
    > [[3 2 1]  
    >  [6 5 4]]

---------------------

## 拷贝与视图

- 完全不复制

   ```python
    a = np.arange(12)
    b = a
    ```

  - 函数传参

- 视图： 不同的数组对象可以共享相同的数据 

  - `c = a.view()`：创建一个视图
  - `s = a[::]`：切片创建一个视图
  - `c.base is a`：True

# 保存文件

-----------------------------------

# 文件存取

- np.savetxt & np.loadtext

  ```python
  import numpy as np
  np.loadtxt(fname='', dtype=str, comment='#', delimiter='')
  # fname：文件名
  # dtype：数据类型，默认浮点
  # comment：
  # delimiter：分隔符
  ```

  

- 