data = '1,zlw,男'
MyDict = {}

(MyDict['id'],MyDict['name'],MyDict['sex']) = data.split(',')


print("ID:  "+ MyDict['id'])
print("Name:  "+ MyDict['name'])
print("男:  "+ MyDict['sex'])
