from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql.functions import collect_list, avg, last

spark = (SparkSession
         .builder
         .master('local[1]')
         .appName('selecting_column')
         .getOrCreate())
'''
df = spark.read.load('../data/zipcodes.csv', format='csv', header='true')

# Select Columns From DataFrame
df.select(df.Zipcode, df.City).show()

df.select('Zipcode', 'City').show()

df.select(df['Zipcode'], df['City']).show()

# Select columns by regular expression
df.select(df.colRegex("`^.*City*`")).show()

# By using col() function
df.select(col('Zipcode'), col('City')).show()

# Select All columns from List
# df.select(*columns).show()

# Select All columns
df.select([col for col in df.columns]).show()

df.select("*").show()

# Selects first 3 columns and top 3 rows
df.select(df.columns[:3]).show(3)

# Selects columns 2 to 4  and top 3 rows
df.select(df.columns[2:4]).show(3)


    # collect () vs select ()
    select() is a transformation that returns a new DataFrame and holds the columns
    that are selected whereas collect() is an action that returns the entire data 
    set in an Array to the driver.

dataCollect = df.collect()
print(dataCollect)
'''

data = [
    (("James", None, "Smith"), "OH", "M", "Sales", 3000),
    (("Anna", "Rose", ""), "NY", "F", "Sales", 4600),
    (("Julia", "", "Williams"), "OH", "F", "Finance", 3000),
    (("Maria", "Anne", "Jones"), "NY", "M", "Finance", 3300),
    (("Jen", "Mary", "Brown"), "NY", "M", "Marketing", 3000),
    (("Mike", "Mary", "Williams"), "OH", "M", "Marketing", 2000)
]

schema = StructType([
    StructField('name', StructType([
        StructField('firstname', StringType(), True),
        StructField('middlename', StringType(), True),
        StructField('lastname', StringType(), True)
    ])),
    StructField('state', StringType(), True),
    StructField('gender', StringType(), True),
    StructField('department', StringType(), True),
    StructField('salary', IntegerType(), True)
])

df2 = spark.createDataFrame(data=data, schema=schema)
df2.printSchema()
df2.show(truncate=False)  # shows all columns
df2.select("name").show(truncate=False)
df2.select("name.firstname", "name.lastname").show(truncate=False)
df2.select("name.*").show(truncate=False)

df2.select(collect_list("state")).show(truncate=False)

df2.select(avg("salary")).show()
print("count: "+str(df2.select(avg("salary")).collect()[0][0]))

df2.select(last("salary").alias('last_salary')).show(truncate=False)

df2.registerTempTable('employees')
result = spark.sql('SELECT * FROM employees')
result.show()

spark.stop()
