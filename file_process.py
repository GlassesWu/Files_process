import os, shutil

def file_name(file_dir):
    # 将集合内容按需放入列表中
    filetypelist = ['html', 'iml', 'jpeg', 'png', 'url', 'db', 'xml',
                    'torrent', 'txt', 'jpg', 'PNG', 'JPG']
    for fileroot, filedir, filenames in os.walk(file_dir):
        for filename in filenames:
            filetype = filename.split('.')[-1]
            if filetype in filetypelist:
                print('将要删除文件:' + filename)
                # 将列表内类型的文件删除,使用os.path.join(dir, filename)方法将路径拼接
                os.remove(os.path.join(fileroot,filename))

def file_type(file_dir):
    typelist = []
    # 以列表形式分隔路径、文件名
    for fileroot, filedir, filenames in os.walk(file_dir):
        # 遍历列表中的文件说名
        for filename in filenames:
            # 切片取文件名中的文件类型
            filetype = filename.split('.')[-1]
            # 将文件类型放入列表中
            typelist.append(filetype)
    # 创建集合将列表内容去重
    collections = set(typelist)
    print(collections)

def file_move(old_file_dir, new_file_dir):
    for fileroot, filedir, filenames in os.walk(old_file_dir):
        for filename in filenames:
            # 调用shutil.move(路径1，路径2)
            shutil.move(os.path.join(fileroot, filename), os.path.join(new_file_dir, filename))



# file_type(r'c:\users\1\desktop\新建文件夹')
#file_name(r'c:\users\1\desktop\新建文件夹')
file_move(r'c:\users\1\desktop\新建文件夹', r'c:\users\1\desktop\新建文件夹\新建文件夹')

