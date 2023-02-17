def read(number):
    file = open(f'LibraryAppBooks\\{number}')
    lines = file.read().splitlines()
    book = eval(lines[2:3])
    file.close()
    return book
def write(name,writer,number,year,star,additional,category,group,publisher):
    file = open(f'LibraryAppBooks\\{number}.blf','w')
    x = {'name':name,'writer':writer,'number':number,'year':year,'star':star,'additional':additional,'category':category,'group':group,'publisher':publisher}
    file.write(f'v1.0\n--begin--\n{str(x)}\n--end--')
    file.close()
    return x

def readP(name):
    file = open(f'Pubs\\{name}')
    lines = file.read().splitlines()
    file.close()
    return lines
def writeP(name,number):
    file = open(f'Pubs\\{name}','a')
    file.write(f'{number}\n')
    file.close()

def readC(name):
    file = open(f'Cats\\{name}')
    lines = file.read().splitlines()
    file.close()
    return lines
def writeC(name,number):
    file = open(f'Cats\\{name}','a')
    file.write(f'{number}\n')
    file.close()

def readG(name):
    file = open(f'Groups\\{name}')
    lines = file.read().splitlines()
    file.close()
    return lines[1:]
def writeG(name,number):
    file = open(f'Groups\\{name}','a')
    file.write(f'{number}\n')
    file.close()
