# -*- coding:utf-8 -*-
import threading
import zipfile


def extractFile(zFile, password):
    '''
    破解方法
    :param zFile: 需要破解的文件
    :param password: 尝试密码
    :return:
    '''
    try:
        zFile.extractall(pwd=password)
        print("Found Passwd:", password)
        event.set()
        return password
    except:
        event.wait()
        pass


def main():
    '''
    主函数
    '''
    zFile = zipfile.ZipFile('H:\BaiduNetdiskDownload\YTSU（12）.zip')
    passFile = open("14365003.txt")
    for line in passFile.readlines():
        if event.isSet():
            print("End")
            return
        else:
            password = line.strip('\n')
            t = threading.Thread(target=extractFile, args=(zFile, password))
            t.start()


if __name__ == '__main__':
    event = threading.Event()
    main()
