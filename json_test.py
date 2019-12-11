import pymysql, json

# read JSON file which is in the next parent folder
file = "https://opendata.swiss/api/3/action/package_show?id=regionale-arbeitsmarkte-fur-frauen-und-manner"
json_data=open(file).read()
json_obj = json.loads(json_data)


# do validation and checks before insert
def validate_string(val):
   if val != None:
        if type(val) is int:
            #for x in val:
            #   print(x)
            return str(val).encode('utf-8')
        else:
            return val


# connect to MySQL
con = pymysql.connect(host = 'localhost',user = 'cyrill',passwd = 'Banane99%',db = 'sys')
cursor = con.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS new_table")

# parse json data to SQL insert
for i, item in enumerate(json_obj):
    person = validate_string(item.get("person", None))
    year = validate_string(item.get("year", None))
    company = validate_string(item.get("company", None))

    cursor.execute("INSERT INTO new_table (person,	year,	company) VALUES (%s, %s, %s)", (person,	year, company))

con.commit()
con.close()