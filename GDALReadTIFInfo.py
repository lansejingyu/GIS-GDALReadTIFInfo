# -*- coding: utf-8 -*-
# @Project : GIS
# @File : GDAL-read TIF info
# @IDE：PyCharm
# @Author : KT15
# @Time : 2022/10/12 13:53

from osgeo import gdal
import os


def Files():
	FilePath = input("输入.TIF文件路径+文件名：")
	dataset = gdal.Open(r'' + FilePath)  # 打开已有的GeoTIF文件

	def Blanklines():  # 打印一行空白行，定义一个函数
		print()

	def GetMetadata():  # 读取影像的元数据信息
		print("1.影像的元数据信息:\n", dataset.GetMetadata())

	def GetDescription():  # 获得栅格的描述信息
		print("2.栅格的描述信息:\n", dataset.GetDescription())

	def RasterCount():  # 获得栅格数据集的波段数（获取栅格数目）
		print("3.栅格数据集的波段数(栅格数目):\n", dataset.RasterCount)

	def GetGeoTransform():  # 获得空间参考(栅格数据的六参数:左上角坐标，像元X、Y方向大小，旋转等信息。 要注意，Y方向的像元大小为负值。)
		print("4.空间参考(栅格数据的六参数:左上角坐标，像元X、Y方向大小，旋转等信息。 要注意，Y方向的像元大小为负值。):\n",
			  dataset.GetGeoTransform())

	def RasterSize():  # 影像大小(栅格数据的宽度(X方向上的像素个数),栅格数据的高度(Y方向上的像素个数))
		print("5.影像大小:\n", "X方向上的像素个数:", dataset.RasterXSize, "Y方向上的像素个数:", dataset.RasterYSize)

	def GetProjection():  # 栅格数据的投影信息
		print("6.栅格数据的投影信息:\n", dataset.GetProjection())

	def GetRasterBand():  # 查看波段的基本信息
		print("7.波段的基本信息:")
		print("第一波段:", dataset.GetRasterBand(1))  # 这是函数的参数使用波段的索引值。
		print("第二波段:", dataset.GetRasterBand(2))
		print("第三波段:", dataset.GetRasterBand(3))
		print("第四波段:", dataset.GetRasterBand(4))

	def Size():  # 获取波段大小:波段图像的宽和高（像元为单位）,与使用 RasterXSize() 与 RasterYSize() 获取的值一致;数据类型:是图像中实际数值的数据类型，表示8位无符整型
		print("8.波段大小:波段图像的宽和高（像元为单位）:\n", "宽(X):", dataset.GetRasterBand(1).XSize, "高(Y):",
			  dataset.GetRasterBand(1).YSize, "数据类型:", dataset.GetRasterBand(2).DataType)

	# def GetNoDataValue():
	# 	print(dataset.GetRasterBand(1).GetNoDataValue())

	def Getnum():  # 表示在本波段数值中最大值、最小值
		print("9.本波段数值中最大值、最小值(若结果为None,是因为对于文件格式不会有固有的最大最小值):")
		print("第一波段:")
		print("最大值:", dataset.GetRasterBand(1).GetMaximum(), "最小值:", dataset.GetRasterBand(1).GetMinimum())
		print("第二波段:")
		print("最大值:", dataset.GetRasterBand(2).GetMaximum(), "最小值:", dataset.GetRasterBand(2).GetMinimum())
		print("第三波段:")
		print("最大值:", dataset.GetRasterBand(3).GetMaximum(), "最小值:", dataset.GetRasterBand(3).GetMinimum())
		print("第四波段:")
		print("最大值:", dataset.GetRasterBand(4).GetMaximum(), "最小值:", dataset.GetRasterBand(4).GetMinimum())

	def ComputeRasterMinMax():  # 计算得到当前索引波段的最大最小值
		print("10.计算得到当前索引波段的最大最小值:")
		print("第一波段", dataset.GetRasterBand(1).ComputeRasterMinMax())
		print("第二波段", dataset.GetRasterBand(2).ComputeRasterMinMax())
		print("第三波段", dataset.GetRasterBand(3).ComputeRasterMinMax())
		print("第四波段", dataset.GetRasterBand(4).ComputeRasterMinMax())

	def DataType():  # 图像中实际数值的数据类型,具体数据类型定义在gdalconst模块里。这里的类型是与numpy中的类型对应的。
		'''
		gdalconst与整型的对应值:
		未知或未指定类型 gdalconst.GDT_Unknown 0
		8位无符整型 gdalconst.GDT_Byte 1
		16位无符整型 gdalconst.GDT_UInt16 2
		16位整型 gdalconst.GDT_Int16 3
		32位无符整型 gdalconst.GDT_UInt32 4
		32位整型值 gdalconst.GDT_Int32 5
		32位浮点型 gdalconst.GDT_Float32 6
		64位浮点型 gdalconst.GDT_Float64 7
		16位复数整型 gdalconst.GDT_CInt16 8
		32位复数整型 gdalconst.GDT_CInt32 9
		32位复数浮点型 gdalconst.GDT_CFloat32 10
		64位复数浮点型 gdalconst.GDT_CFloat64 11
		'''
		print("11.获取当前索引波段数值的数据类型:")
		print("第一波段数值的数据类型:", (dataset.GetRasterBand(1)).DataType)
		print("第二波段数值的数据类型:", (dataset.GetRasterBand(2)).DataType)
		print("第三波段数值的数据类型:", (dataset.GetRasterBand(3)).DataType)
		print("第四波段数值的数据类型:", (dataset.GetRasterBand(4)).DataType)
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
64位复数浮点型gdalconst.GDT_CFloat64 11
''')

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
	GetProjection()
	Blanklines()
	GetRasterBand()
	Blanklines()
	Size()
	Blanklines()
	Getnum()
	Blanklines()
	ComputeRasterMinMax()
	Blanklines()
	DataType()
	Files()


Files()
# os.system('pause')
