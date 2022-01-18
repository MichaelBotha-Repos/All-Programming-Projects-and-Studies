import json

fun_list = ["amy", 123, 15.15]

# Serialising the list object into JSON = text
fun_list_json = json.dumps(fun_list)
print(type(fun_list_json))

# Deserialising the json/text into a Python list
fun_list_again = json.loads(fun_list_json)
print(type(fun_list_again))
