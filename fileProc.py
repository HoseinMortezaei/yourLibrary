def read(number):
    file = open(f'{number}.blf')
    lines = file.read().splitlines()
    book = eval(lines[2:3])
    return book
def write(name,writer,number,year,star,additional,category,group,publisher):
    file = open(f'LibraryAppBooks\\{number}.blf','w')
    x = {'name':name,'writer':writer,'number':number,'year':year,'star':star,'additional':additional,'category':category,'group':group,'publisher':publisher}
    file.write(f'v1.0\n--begin--\n{str(x)}\n--end--')
    file.close()
    return x