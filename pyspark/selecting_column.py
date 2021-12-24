from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

spark = (SparkSession
         .builder
         .master('local[1]')
         .appName('selecting_column')
         .getOrCreate())

df = spark.read.load('../data/zipcodes.csv', format='csv', header='true')

# Select Columns From DataFrame
df.select(df.Zipcode, df.City).show()

df.select('Zipcode', 'City').show()

df.select(df['Zipcode'], df['City']).show()

# Select columns by regular expression
df.select(df.colRegex("`^.*City*`")).show()

# By using col() function
from pyspark.sql.functions import col

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

data = [
    (("James", None, "Smith"), "OH", "M"),
    (("Anna", "Rose", ""), "NY", "F"),
    (("Julia", "", "Williams"), "OH", "F"),
    (("Maria", "Anne", "Jones"), "NY", "M"),
    (("Jen", "Mary", "Brown"), "NY", "M"),
    (("Mike", "Mary", "Williams"), "OH", "M")
]

schema = StructType([
    StructField('name', StructType([
        StructField('firstname', StringType(), True),
        StructField('middlename', StringType(), True),
        StructField('lastname', StringType(), True)
    ])),
    StructField('state', StringType(), True),
    StructField('gender', StringType(), True)
])

df2 = spark.createDataFrame(data=data, schema=schema)
df2.printSchema()
df2.show(truncate=False)  # shows all columns
df2.select("name").show(truncate=False)
df2.select("name.firstname", "name.lastname").show(truncate=False)
df2.select("name.*").show(truncate=False)

'''
    # collect () vs select ()
    select() is a transformation that returns a new DataFrame and holds the columns
    that are selected whereas collect() is an action that returns the entire data 
    set in an Array to the driver.
'''
dataCollect = df.collect()
print(dataCollect)

spark.stop()
