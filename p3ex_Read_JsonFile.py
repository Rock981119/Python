import json

#api_result_file = "./Halloween.json"
#api_result_read = open("./Halloween.json")
#上一个程序中，我们已经将返回的内容输入到了Halloween.json这个文件中了，并以json格式保存了。
#results_file = results_file.write(str(json.dumps(results)))
#现在我们在当前的程序中读取这个Json文件，并非只用.read（）方法，而是使用json.load()去读取已open的对象，相当于用read（）读取一样。
api_result_matadata = json.load(open("./Halloween.json"))
print(api_result_matadata)

#将其中名为color的这个字典赋予api_taget1
api_taget1 = api_result_matadata["color"]
print("\n\n")
print(f"Color dict include:\n\t{api_taget1}")

#如何输出多级字典
api_taget2 = api_result_matadata["description"]["tags"]
print(f"Description has subkey dict:\n\t{api_taget2}")