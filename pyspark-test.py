from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
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
# top_data = sc.parallelize("afghajshfqwuefsajdfaadfae")
# top_n_data = (
#     top_data.map(lambda x: (x, 1))
#     .reduceByKey(lambda x, y: x+y)
# )
# print(top_n_data.collect())
# top1 = top_n_data.top(30, key=lambda x: x[1])  # x[1]是(key,value)中的value
# print(top1)

# sparksql
# Initialise spark context.

spark = (SparkSession.builder
         .master('local[*]').config("spark.app.name", "app_spark_name")
         .enableHiveSupport()
         .getOrCreate()
         )

# data_df = spark.read.json('file:///D:/1Info/project/python/python_learn/input/data.json')
# data_df.show()
# data_df.select("name", data_df["id"]+1).show()

# sql
# data_df.registerTempTable("t_datajson")
# spark.sql("select name,id from t_datajson where id >2").show()
# spark.sql("select * from t_datajson limit 3").show()
# group_df = spark.sql(
#     "select name,count(1) as count from t_datajson group by name")
# all_df = spark.sql("select * from t_datajson")

# group_json = group_df.toJSON()
# print(group_json.collect())

# create table
# retrunstr = spark.sql("create table t_ren1 (id int ,name string)")
# print(retrunstr.collect())
# spark.sql("INSERT INTO t_ren VALUES (1,'zhang'), (2,'tank') ")
# spark.sql("select * from t_ren").show()
data_ren = spark.sql("select * from t_ren")
data_dict = dict(data_ren.collect())
print(data_dict)
