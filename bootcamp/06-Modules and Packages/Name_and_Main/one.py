def func():
    print('hi from one.py function!!')

print('hi from one.py file')

if __name__ == "__main__":
    print('one.py is being run directly')
else:
    print("one.py is imported into another module. name value is{}".format(__name__))