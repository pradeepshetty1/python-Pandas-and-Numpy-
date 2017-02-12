import zipfile

zi = zipfile.ZipFile('myTest.zip','w')
zi.write('file1.txt')
zi.write('file2.txt')

zi.close()
print 'Namelist',zi.namelist()