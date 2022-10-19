# GIS-GDALReadTIFInfo

.TIF文件信息获取
通过gdal库实现.TIF文件信息获取
![image](https://user-images.githubusercontent.com/50358622/196157120-fedcaa4b-98e4-49f0-bc4f-3def5a1c1509.png)

当前功能：  
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
---------------------提示:gdalconst与整型的对应值:---------------------  
未知或未指定类型 gdalconst.GDT_Unknown 0  
8位无符整型 gdalconst.GDT_Byte 1  
16位无符整型 gdalconst.GDT_UInt16 2  
16位整型 gdalconst.GDT_Int16 3  
32位无符整型 gdalconst.GDT_UInt32 4  
32位整型值 gdalconst.GDT_Int32 5  
32位浮点型gdalconst.GDT_Float32 6  
64位浮点型gdalconst.GDT_Float64 7  
16位复数整型gdalconst.GDT_CInt16 8  
32位复数整型gdalconst.GDT_CInt32 9  
32位复数浮点型gdalconst.GDT_CFloat32 10  
64位复数浮点型gdalconst.GDT_CFloat64 11