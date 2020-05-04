from pyspark import SparkConf, SparkContext
import random

# 注意配置spark环境变量

conf = SparkConf().setMaster("local[*]").setAppName("APP_Qiang")

sc = SparkContext.getOrCreate(conf)

# mylist = [1, 2, 3, 4, 5]
# rdd = sc.parallelize(mylist)

# 转换后数据
# print(rdd.collect())
# 分区数
# print(rdd.getNumPartitions())
# 按照分区打印数据
# print(rdd.glom().collect())

# 从文件中读取
# mypath = "file:///D:/1Info/project/python/python_learn/Data/wc.txt"
# rdd = sc.textFile(mypath)
# print(rdd.collect())
# result = rdd.(lambda x: (x, 1))
# print(rdd)

# 从HDFS中读取
# hdfs_path = "hdfs://input/wc.txt"
# rdd = sc.textFile(hdfs_path)
# print(rdd.collect())

# 读取目录下的所有文件
# file_path = "file:///D:/1Info/project/python/python_learn/Data"
# rdd = sc.wholeTextFiles(file_path)
# print(rdd.take(2))

# mapPartitions 根据分区计算数据 入是迭代器，出也是迭代器
# rdd_data = sc.parallelize("asdjflqwedhfhaugdlfa;jgqwiuerhasdfaksdfj;")
# print(rdd_data.getNumPartitions())
# print(rdd_data.glom().collect())
# rdd_result = (
#     rdd_data.map(lambda x: (x, 1))
#     .mapPartitions(
#         lambda iter: map(lambda arr: (
#             (random.randint(1, 100), arr[0]), arr[1]), iter))
# )

# print(rdd_result.collect())

# 算子 map flatMap filter distinct sample sortBy
# mypath = "file:///D:/1Info/project/python/python_learn/Data/wc.txt"
# rdd = sc.textFile(mypath)
# rdd_result = rdd.map(lambda x: (x, 1))
# print(rdd_result.collect())
# print('*'*40)
# x_rdd = rdd.flatMap(lambda x: x.split(' ')).map(
#     lambda x: (x, 1)).reduceByKey(lambda x, y: x+y)
# print(x_rdd.collect())
# x_rdd.saveAsTextFile("file:///D:/1Info/project/python/python_learn/output/wc_count.txt")

# 算子 groupByKey reduceByKey sortByKey aggregateByKey sampleByKey
mypath = "file:///D:/1Info/project/python/python_learn/Data/wc.txt"
rdd = sc.textFile(mypath)
rdd_result = (
    rdd
    .flatMap(lambda x: x.split(" "))
    .map(lambda x: x.lower())
    .map(lambda x: (x, 1))
)
# print(rdd_result.collect())
# groupByKey
# print(rdd_result.groupByKey().collect())
# reduceByKey
# rdd_reduce = rdd_result.reduceByKey(lambda x, y: x+y)
# print(rdd_reduce.collect())
# sortByKey
# print(rdd_reduce.sortByKey(ascending=False).collect())
# aggregateByKey
# print(rdd_result.aggregateByKey(0, lambda x, y: x+y, lambda x, y: x+y).collect())

# RDD之间使用的API
# union并集 intersection交集 substract差集 cartesian笛卡尔积


# RDD 的join
# join leftOuterJoin rightOuterJoin fullOuterJoin


# action 算子
# 1. collect() take() first()
# 2.输出 foreach foreachPartition
# 3.保存文件到外部存储系统 saveAsTextFile()


# TOP n
top_data = sc.parallelize("afghajshfqwuefsajdfaadfae")
top_n_data = (
    top_data.map(lambda x: (x, 1))
    .reduceByKey(lambda x, y: x+y)
)
print(top_n_data.collect())
top1 = top_n_data.top(30, key=lambda x: x[1])  # x[1]是(key,value)中的value
print(top1)