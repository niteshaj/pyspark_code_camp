from pyspark.sql import functions as F
from pyspark.sql import SparkSession
from pyspark.sql import Row

spark = SparkSession \
    .builder \
    .master("local[1]") \
    .appName("SparkExamples.com") \
    .getOrCreate()

# print(spark)

# text_file = spark.read.text("NOTICE.txt")
#
# print(f'****************** {text_file.count()}')
# print(f'****************** {text_file.first()}')


f1 = Row(original_title='Eroica', budget='13393950', year=1992)
f2 = Row(original_title='Night World', budget='1255930', year=1998)
f3 = Row(original_title='Night World', budget='1255930', year=1998)

films = [f1, f2, f3]

df = spark.createDataFrame(films)

df = df.withColumn("new_column", F.lit(2020))
df.show()

df.select("original_title").show()

# print(df.dtypes)
# print(df.schema)
# print(df.take(1))
# print(df.head())
# print(df.first())

# Remove duplicate
# dfnd = df.dropDuplicates()
# dfnd.show()

# df = spark.read \
#    .option("header", True) \
#    .csv("../data/zipcodes.csv")

df = spark.read \
    .load('../data/zipcodes.csv', format='csv', inferschema='true', header='true')

df.groupby("ZipCodeType") \
    .count() \
    .show()

df.filter(df['Lat'] > 35).show()

# saving the dataframe as JSON
# df.select("Zipcode", "ZipCodeType")\
#     .write\
#     .save("./Zipcode_ZipCodeType.json", format="json")

spark.stop()
