import one

print('hi from two.py file')

one.func()

if __name__ == '__main__':
    print('two.py is being run directly')
else:
    print("one.py is imported into another module. name value is {}".format(__name__))