import os

def readFileTest():
    #fp = open('gifts.csv','r')
    fp = open('F:\squarks\Training\Edureka\python\practicals\project\Module2\gifts.csv','r')

    count = 0
    for line in fp:
        count+=1

    print count

    if not fp.closed:
        print 'File not closed'
        fp.close()


def readFileTestWithOpen():
    with open('gifts.csv','r') as fp:
        count = 0
        for line in fp:
            count+=1

        print count

    if not fp.closed:
        print 'File not closed'
        fp.close()

def fileAppendTest():
    with open('file_forAppend.txt','a') as fp_append:
        with open('source_file.txt','r') as fp_source:
            for line in fp_source:
                fp_append.write(line)


def get_current_wd():
    print 'Current Working Directory is : ',os.getcwd()

def get_file_list():
    for file_list in os.listdir(os.getcwd()):
        print file_list

#readFileTest()
#readFileTestWithOpen()
#fileAppendTest()
#get_current_wd()
get_file_list()







