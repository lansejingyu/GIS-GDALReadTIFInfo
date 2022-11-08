# GIS-GDALReadTIFInfo

通过gdal库实现.tif / .shp文件信息的获取，绘制，计算。
![image](https://user-images.githubusercontent.com/50358622/196157120-fedcaa4b-98e4-49f0-bc4f-3def5a1c1509.png)

----v1.0.4  
新增以下功能:  
1.增加“读取SHP的投影信息”功能：.GetSpatialRef()

修复:  
1.修改已知bug;  
2.优化代码。  

----v1.0.3  
新增以下功能:  
1.自动识别.tif / .shp文件类型;  
1.获取.shp文件属性;  
2.实现绘制.shp文件（独立窗口）;  
![image](https://user-images.githubusercontent.com/50358622/198241624-2b7cca2e-f465-46d2-9a5f-8de0ffc543e4.png)

修复:  
1.修改已知bug;  
2.调整个别函数功能，不影响正常使用。  

----v1.0.2  
新增两个功能：    
1.计算当前栅格影像面积；  
2.获取当前栅格影像各波段的nodata值。

修复：  
1.修改已知的bug；  
2.修改部分注释说明。

当前全部功能：  
1.获取影像的元数据信息  
2.获取栅格的描述信息  
3.获取栅格数据集的波段数（获取栅格数目）  
4.获取空间参考(栅格数据的六参数:左上角坐标，像元X、Y方向大小，旋转等信息。 要注意，Y方向的像元大小为负值。)  
5.获取影像大小(栅格数据的宽度(X方向上的像素个数),栅格数据的高度(Y方向上的像素个数))  
6.获取栅格数据的投影信息  
7.获取波段的基本信息  
8.获取波段大小:波段图像的宽和高（像元为单位）,与使用 RasterXSize() 与 RasterYSize() 获取的值一致;数据类型:  
是图像中实际数值的数据类型，表示8位无符整型  
9.获取当前本波段数值中最大值、最小值  
10.计算得到当前索引波段的最大最小值  
11.获取图像中实际数值的数据类型  
12.计算当前栅格影像面积；  
13.获取当前栅格影像各波段的nodata值。
