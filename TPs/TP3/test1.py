import pyspark
from pyspark import SparkContext
sc =SparkContext()
nums= sc.parallelize([1,2,3,4])	
squared = nums.map(lambda x: x*x).collect()
for num in squared:
    print('%i ' % (num))
