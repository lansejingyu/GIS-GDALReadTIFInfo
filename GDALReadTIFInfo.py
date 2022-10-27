# -*- coding: utf-8 -*-
# @Project : GIS
# @File : GDAL-read TIF info
# @IDE：PyCharm
# @Author : KT15
# @Time : 2022/10/12 13:53

from osgeo import gdal
import shapefile
from matplotlib import pyplot as plt
import os


def Files():
	FilePath = input('''----------目前仅支持.tif / .shp文件----------
请输入栅格影像文件路径+文件名(如:E:\TIF\masaike\K50F038012.tif)：''')
	if ".tif" in FilePath:
		datasetTif = gdal.Open(r'' + FilePath)  # 使用gdal库打开已有的GeoTIF文件
	elif ".shp" in FilePath:
		datasetShp = shapefile.Reader(r'' + FilePath)  # 使用shapefile库打开已有的shp文件
	print("")

	if ".tif" in FilePath:
		def Blanklines():  # 打印一行空白行，定义一个函数
			print()

		def GetMetadata():  # 获取栅格影像的元数据信息
			print("1.栅格影像的元数据信息:\n", datasetTif.GetMetadata())

		def GetDescription():  # 获取栅格的描述信息
			print("2.栅格影像的描述信息:\n", datasetTif.GetDescription())

		def RasterCount():  # 获取栅格数据集的波段数（获取栅格数目）
			print("3.栅格影像数据集的波段数(栅格数目):\n", datasetTif.RasterCount)

		def GetGeoTransform():  # 获取空间参考(栅格数据的六参数:左上角坐标，像元X、Y方向大小，旋转等信息。 要注意，Y方向的像元大小为负值。)
			print(
				"4.栅格影像空间参考(栅格数据的六参数:左上角坐标，像元X、Y方向大小，旋转等信息。 要注意，Y方向的像元大小为负值。):\n",
				datasetTif.GetGeoTransform())

		def RasterSize():  # 获取影像大小(栅格数据的宽度(X方向上的像素个数),栅格数据的高度(Y方向上的像素个数))
			print("5.栅格影像大小:\n", "X方向上的像素个数:", datasetTif.RasterXSize, "\n Y方向上的像素个数:",
				  datasetTif.RasterYSize)

		def GetAcreage():  # 计算当前栅格影像面积
			print("6.栅格影像面积:\n",
				  datasetTif.RasterXSize * datasetTif.RasterYSize * (datasetTif.GetGeoTransform())[1:2][0] *
				  (datasetTif.GetGeoTransform())[1:2][
					  0] / 1000000, "平方千米")

		def GetProjection():  # 获取栅格数据的投影信息
			print("7.栅格影像数据的投影信息:\n", datasetTif.GetProjection())

		def GetRasterBand():  # 获取波段的基本信息
			print("8.栅格影像波段的基本信息:")
			print("第一波段:", datasetTif.GetRasterBand(1))  # 这是函数的参数使用波段的索引值。
			print("第二波段:", datasetTif.GetRasterBand(2))
			print("第三波段:", datasetTif.GetRasterBand(3))
			print("第四波段:", datasetTif.GetRasterBand(4))

		def GetSize():  # 获取波段大小:波段图像的宽和高（像元为单位）,与使用 RasterXSize() 与 RasterYSize() 获取的值一致;数据类型:是图像中实际数值的数据类型，表示8位无符整型
			print("9.栅格影像波段大小:波段图像的宽和高（像元为单位）:\n", "宽(X):", datasetTif.GetRasterBand(1).XSize,
				  "高(Y):",
				  datasetTif.GetRasterBand(1).YSize, "数据类型:", datasetTif.GetRasterBand(2).DataType)

		def GetNoDataValue():  # 获取当前栅格影像各波段的nodata值。
			print("10.栅格影像的nodata值:")
			print("第一波段:", datasetTif.GetRasterBand(1).GetNoDataValue())
			print("第二波段:", datasetTif.GetRasterBand(2).GetNoDataValue())
			print("第三波段:", datasetTif.GetRasterBand(3).GetNoDataValue())
			print("第四波段:", datasetTif.GetRasterBand(4).GetNoDataValue())
			print('''
			提示：
			对于GeoTIFFs，nodata值存储在TIFF tag_GDAL_NODATA TIFF标记中。新创建的GeoTIFF文件可以没有nodata值（没有标记），但一旦设置并存储了nodata值，就只能为其提供新值，不能将其删除。也不能设置为数据类型范围之外的值；对于8位数据传递 nan ， -inf 或 256 到 GDALSetNoDataValue() 与传递0具有相同的效果。
			''')

		def Getnum():  # 获取当前本波段数值中最大值、最小值
			print("11.当前波段数值中最大值、最小值(若结果为None,是因为对于文件格式不会有固有的最大最小值):")
			print("第一波段:")
			print("最大值:", datasetTif.GetRasterBand(1).GetMaximum(), "最小值:",
				  datasetTif.GetRasterBand(1).GetMinimum())
			print("第二波段:")
			print("最大值:", datasetTif.GetRasterBand(2).GetMaximum(), "最小值:",
				  datasetTif.GetRasterBand(2).GetMinimum())
			print("第三波段:")
			print("最大值:", datasetTif.GetRasterBand(3).GetMaximum(), "最小值:",
				  datasetTif.GetRasterBand(3).GetMinimum())
			print("第四波段:")
			print("最大值:", datasetTif.GetRasterBand(4).GetMaximum(), "最小值:",
				  datasetTif.GetRasterBand(4).GetMinimum())

		def ComputeRasterMinMax():  # 计算得到当前索引波段的最大最小值
			print("12.计算得到当前索引波段的最大最小值:")
			print("第一波段", datasetTif.GetRasterBand(1).ComputeRasterMinMax())
			print("第二波段", datasetTif.GetRasterBand(2).ComputeRasterMinMax())
			print("第三波段", datasetTif.GetRasterBand(3).ComputeRasterMinMax())
			print("第四波段", datasetTif.GetRasterBand(4).ComputeRasterMinMax())

		def DataType():  # 获取栅格影像中实际数值的数据类型,具体数据类型定义在gdalconst模块里。这里的类型是与numpy中的类型对应的。
			print("13.获取当前索引波段数值的数据类型:")
			print("第一波段数值的数据类型:", (datasetTif.GetRasterBand(1)).DataType)
			print("第二波段数值的数据类型:", (datasetTif.GetRasterBand(2)).DataType)
			print("第三波段数值的数据类型:", (datasetTif.GetRasterBand(3)).DataType)
			print("第四波段数值的数据类型:", (datasetTif.GetRasterBand(4)).DataType)
			print('''
	提示:
	gdalconst与整型的对应值:
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
	64位复数浮点型gdalconst.GDT_CFloat64 11''')

		GetMetadata()
		Blanklines()
		GetDescription()
		Blanklines()
		RasterCount()
		Blanklines()
		GetGeoTransform()
		Blanklines()
		RasterSize()
		Blanklines()
		GetAcreage()
		Blanklines()
		GetProjection()
		Blanklines()
		GetRasterBand()
		Blanklines()
		GetSize()
		Blanklines()
		GetNoDataValue()
		Blanklines()
		Getnum()
		Blanklines()
		ComputeRasterMinMax()
		Blanklines()
		DataType()
		Blanklines()
		Files()

	elif ".shp" in FilePath:
		def Blanklines():  # 打印一行空白行，定义一个函数
			print()

		def ShapeType():  # 输出shp类型
			print("1.当前.shp文件类型:\n", str(datasetShp.shapeType))
			print('''
	提示:
	----shp类型信息----
	文件长度的值是用16位字表示的文件总长度(包括组成文件头的50个16位字)。shape文件中所有的非空shape必须是相同类型的。以下是shape类型的值：
	Value       Shape Type
	  0          Null Shape
	  1          Point
	  3          PolyLine
	  5          Polygon
	  8          MultiPoint
	  11         PointZ
	  13         PolyLineZ
	  15         PolygonZ
	  18         MultiPointZ
	  21         PointM
	  23         PolyLineM
	  25         PolygonM
	  28         MultiPointM
	  31         MultiPatch
	
	未列入上述表中的Shape type有2、4、6以及33等等，这些是做为保留以备将来使用。目前每个shape文件被限定为只能包含上述类型的一种，将来shape文件可能会被允许包含一种以上的shape类型。''')

		def Encoding():  # 输出shp文件编码
			print("2.当前.shp文件编码:\n", datasetShp.encoding)

		def Bbox():  # 输出当前.shp的文件范围（外包矩形）
			print("3.当前.shp文件范围(外包矩形):\n", datasetShp.bbox)

		def BorderPoints():# 返回第1个对象的所有点坐标
			border = datasetShp.shapes()  # .shapes()读取全部几何数据信息，存放着该文件中所有对象的 几何数据,border是一个列表
			border_points = border[0].points  # 返回第1个对象的所有点坐标
			print("4.当前.shp文件所有点坐标:\n", border_points)
		def NumRecords():  # 输出shp文件的要素数据
			print("5.当前.shp文件的要素数据:\n", datasetShp.numRecords)

		def Fields():  # 输出所有字段信息
			print("6.当前.shp文件所有字段信息:\n", datasetShp.fields)

		def Records():  # 输出所有属性表
			print("7.当前.shp文件所有属性表:\n", datasetShp.records())
			print('''
	提示:
	----shp属性表字段信息----
	字段索引     字段类型
	  C         字符,文字
	  N         数字,带或不带小数
	  F         浮动(与'N'相同)
	  L         逻辑，表示布尔值True / False值
	  D         日期
	  M         备忘录，在GIS中没有意义，而是xbase规范的一部分。
	''')

		def Plt():
			choose=input("是否绘制.shp文件矢量范围? (y/n):")
			if choose=="y":
				border = datasetShp.shapes()  # .shapes()读取全部几何数据信息，存放着该文件中所有对象的 几何数据,border是一个列表
				border_points = border[0].points  # 返回第1个对象的所有点坐标
				# print("当前.shp文件所有点坐标:",border_points)
				x, y = zip(*border_points)  # x=(x1,x2,x3,…) y=(y1,y2,y3,…)
				fig, ax = plt.subplots()  # 生成一张图和一张子图
				# plt.plot(x,y,'k-') # x横坐标 y纵坐标 ‘k-’线性为黑色
				plt.plot(x, y, color='#6666ff', label='fungis')  # x横坐标 y纵坐标 ‘k-’线性为黑色
				ax.grid()  # 添加网格线
				ax.axis('equal')
				plt.show()

		ShapeType()
		Blanklines()
		Encoding()
		Blanklines()
		Bbox()
		Blanklines()
		BorderPoints()
		Blanklines()
		NumRecords()
		Blanklines()
		Fields()
		Blanklines()
		Records()
		Blanklines()
		Plt()
		Blanklines()

		Files()

	else:
		def Blanklines():  # 打印一行空白行，定义一个函数
			print()
		print("请选择正确的栅格影像文件!(目前仅支持.tif / .shp文件)")
		Blanklines()
		Files()


Files()
# os.system('pause')
