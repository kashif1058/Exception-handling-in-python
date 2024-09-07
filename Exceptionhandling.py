# Exception Handling

fruit_list= ["apple", "banana","grapes"]
fruit_list[3]

# catching exceptions

try:
    file = open("a_file.txt")
except:
    print("An error occurred")
    file = open("a_file.txt" ,"w")



try:
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    print(a_dict["bdfjd"])
except FileNotFoundError:
    print("Sorry, the file does not exist.")
    file = open("a_file.txt" ,"w")
except KeyError:
    print("Sorry, the key does not exist.")
except KeyError as error_message:
    print(f"Sorry, the key does not exist: {error_message}")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file was closed")