'''this antivirus is made by suhani
    antivirus database is used of anic'''
#importing hash library
import hashlib
import os


#global variable
malware_hashes=list(open("./virushash.txt","r").read().split('\n'))
virusinfo=list(open("./virusinfo.txt","r").read().split('\n'))



#get hash of the file
def sha256_hash(filename):
    try:
        with open(filename,"rb") as f:
            bytes=f.read()
            sha256hash=hashlib.sha256(bytes).hexdigest()
            f.close()
            return sha256hash
    except:
        return 0


#malware detection by hash
def malware_checker(pathoffile):
    global malware_hashes
    global virusinfo

    hash_givenfile=sha256_hash(pathoffile)
    counter=0


    for i in malware_hashes:
        if i==hash_givenfile:
            return virusinfo[counter]
        counter+=1
    return 0


#malware detection in folder
virusname=[]
viruspath=[]

#list of files and it scans all for viruses
def virusscanner(path):

    #get the list of all the files in directory tree at given path
    dir_list=list()
    for (dirpath, dirnames, filenames) in os.walk(path):
        dir_list += [os.path.join(dirpath, file) for file in filenames]

    for i in dir_list:

        if malware_checker(i) != 0:
            print(i)
            virusname.append(malware_checker(i)+" :: file :: "+i)
            viruspath.append(i)


#virus remover
def virusremover(path):
    virusscanner(path)
    if viruspath:
        for i in viruspath:
            os.remove(i)
    else:
        return 0




#virusremover("C:\\Users\\suhan\\Desktop\\testfile")
#print(viruspath)

def junkfileremover():

    #temp files remover

    temp_list=list()

    # windows username
    username = os.environ.get('USERNAME').upper().split(" ")
    for (dirpath, dirnames, filename) in os.walk("C:\\Windows\\Temp"):
        temp_list+=[os.path.join(dirpath,file) for file in filename]
        temp_list+=[os.path.join(dirpath,file) for file in dirnames]

    for (dirpath, dirnames, filename) in os.walk("C:\\Users\\{}~1\\AppData\\Local\\Temp".format(username[0])):
        temp_list+=[os.path.join(dirpath,file) for file in filename]
        temp_list+=[os.path.join(dirpath,file) for file in dirnames]

    for (dirpath, dirnames, filename) in os.walk("C:\\Windows\\Prefetch"):
        temp_list+=[os.path.join(dirpath,file) for file in filename]
        temp_list+=[os.path.join(dirpath,file) for file in dirnames]

    print(temp_list)

    if temp_list:

        for i in temp_list:
            print(i)

            try:
                os.remove(i)

            except:
                pass

            try:
                os.rmdir(i)

            except:
                pass

    else:
        return 0

#rambooster

def rambooster():
    tasklist=["notepad.exe","chrome.exe","AnyDesk.exe","TeamViewer_Service.exe","msedge.exe","cmd.exe","IDMan.exe"]

# task kill
    for i in tasklist:

        os.system("taskkill /f /im {}".format(i))


#dont run chrome will end !!!!!!!!!!!!!!!!
#rambooster()


def FlowDetectorIo(self, path, bit_size):
    with open("---------------", "r") as rFile:
        io = rFile.readlines()
        rFile.close()

    with open(path, "rb") as rFile:
        nj = list(rFile.read())
        rFile.close()

    njStr = ''

    for i in nj:
        njStr += str(i)

    bX = 0

    for f in io:
        for i in range(0, len(f), bit_size):
            if njStr.find(f[i:i + bit_size]) != -1:
                bX += 1

        if flen := len(f) / bit_size:
            prLen = (bX / flen) * 100

    return prLen


#print(FlowDetectorIo("-------------",4))