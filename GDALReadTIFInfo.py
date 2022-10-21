# -*- coding: utf-8 -*-
# @Project : GIS
# @File : GDAL-read TIF info
# @IDE：PyCharm
# @Author : KT15
# @Time : 2022/10/12 13:53

from osgeo import gdal
import os


def Files():
	FilePath = input("请输入.TIF文件路径+文件名(如:E:\TIF\masaike\K50F038012.tif)：")
	dataset = gdal.Open(r'' + FilePath)  # 打开已有的GeoTIF文件
	print("")

	def Blanklines():  # 打印一行空白行，定义一个函数
		print()

	def GetMetadata():  # 获取栅格影像的元数据信息
		print("1.栅格影像的元数据信息:\n", dataset.GetMetadata())

	def GetDescription():  # 获取栅格的描述信息
		print("2.栅格影像的描述信息:\n", dataset.GetDescription())

	def RasterCount():  # 获取栅格数据集的波段数（获取栅格数目）
		print("3.栅格影像数据集的波段数(栅格数目):\n", dataset.RasterCount)

	def GetGeoTransform():  # 获取空间参考(栅格数据的六参数:左上角坐标，像元X、Y方向大小，旋转等信息。 要注意，Y方向的像元大小为负值。)
		print(
			"4.栅格影像空间参考(栅格数据的六参数:左上角坐标，像元X、Y方向大小，旋转等信息。 要注意，Y方向的像元大小为负值。):\n",
			dataset.GetGeoTransform())

	def RasterSize():  # 获取影像大小(栅格数据的宽度(X方向上的像素个数),栅格数据的高度(Y方向上的像素个数))
		print("5.栅格影像大小:\n", "X方向上的像素个数:", dataset.RasterXSize, "\n Y方向上的像素个数:",
			  dataset.RasterYSize)

	def GetAcreage():  # 计算当前栅格影像面积
		print("6.栅格影像面积:\n", dataset.RasterXSize * dataset.RasterYSize * (dataset.GetGeoTransform())[1:2][0] *
			  (dataset.GetGeoTransform())[1:2][
				  0] / 1000000, "平方千米")

	def GetProjection():  # 获取栅格数据的投影信息
		print("7.栅格影像数据的投影信息:\n", dataset.GetProjection())

	def GetRasterBand():  # 获取波段的基本信息
		print("8.栅格影像波段的基本信息:")
		print("第一波段:", dataset.GetRasterBand(1))  # 这是函数的参数使用波段的索引值。
		print("第二波段:", dataset.GetRasterBand(2))
		print("第三波段:", dataset.GetRasterBand(3))
		print("第四波段:", dataset.GetRasterBand(4))

	def GetSize():  # 获取波段大小:波段图像的宽和高（像元为单位）,与使用 RasterXSize() 与 RasterYSize() 获取的值一致;数据类型:是图像中实际数值的数据类型，表示8位无符整型
		print("9.栅格影像波段大小:波段图像的宽和高（像元为单位）:\n", "宽(X):", dataset.GetRasterBand(1).XSize, "高(Y):",
			  dataset.GetRasterBand(1).YSize, "数据类型:", dataset.GetRasterBand(2).DataType)

	def GetNoDataValue():  # 获取当前栅格影像各波段的nodata值。
		print("10.栅格影像的nodata值:")
		print("第一波段:", dataset.GetRasterBand(1).GetNoDataValue())
		print("第二波段:", dataset.GetRasterBand(2).GetNoDataValue())
		print("第三波段:", dataset.GetRasterBand(3).GetNoDataValue())
		print("第四波段:", dataset.GetRasterBand(4).GetNoDataValue())
		print('''
	提示：
	对于GeoTIFFs，nodata值存储在TIFF tag_GDAL_NODATA TIFF标记中。新创建的GeoTIFF文件可以没有nodata值（没有标记），但一旦设置并存储了nodata值，就只能为其提供新值，不能将其删除。也不能设置为数据类型范围之外的值；对于8位数据传递 nan ， -inf 或 256 到 GDALSetNoDataValue() 与传递0具有相同的效果。
	''')

	def Getnum():  # 获取当前本波段数值中最大值、最小值
		print("11.当前波段数值中最大值、最小值(若结果为None,是因为对于文件格式不会有固有的最大最小值):")
		print("第一波段:")
		print("最大值:", dataset.GetRasterBand(1).GetMaximum(), "最小值:", dataset.GetRasterBand(1).GetMinimum())
		print("第二波段:")
		print("最大值:", dataset.GetRasterBand(2).GetMaximum(), "最小值:", dataset.GetRasterBand(2).GetMinimum())
		print("第三波段:")
		print("最大值:", dataset.GetRasterBand(3).GetMaximum(), "最小值:", dataset.GetRasterBand(3).GetMinimum())
		print("第四波段:")
		print("最大值:", dataset.GetRasterBand(4).GetMaximum(), "最小值:", dataset.GetRasterBand(4).GetMinimum())

	def ComputeRasterMinMax():  # 计算得到当前索引波段的最大最小值
		print("12.计算得到当前索引波段的最大最小值:")
		print("第一波段", dataset.GetRasterBand(1).ComputeRasterMinMax())
		print("第二波段", dataset.GetRasterBand(2).ComputeRasterMinMax())
		print("第三波段", dataset.GetRasterBand(3).ComputeRasterMinMax())
		print("第四波段", dataset.GetRasterBand(4).ComputeRasterMinMax())

	def DataType():  # 获取栅格影像中实际数值的数据类型,具体数据类型定义在gdalconst模块里。这里的类型是与numpy中的类型对应的。
		print("13.获取当前索引波段数值的数据类型:")
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
	Files()


Files()
# os.system('pause')
