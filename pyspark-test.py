from pyspark import SparkConf, SparkContext

##注意配置spark环境变量

conf = SparkConf().setMaster("local[*]").setAppName("APP_Qiang")

sc = SparkContext.getOrCreate(conf)

mylist = [1, 2, 3, 4, 5]
rdd = sc.parallelize(mylist)

print(rdd.collect())
print(rdd.getNumPartitions())