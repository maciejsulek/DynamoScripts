def PurgeDir(parent, extensions):
    for root, dirs, files in os.walk(parent):                                      
        for item in files:                                              
            filespec = os.path.join(root, item)
            for i in extensions:
                if filespec.endswith(i):
                    os.unlink(filespec)
        for item in dirs:
            PurgeDir(os.path.join(root, item), extensions)
            shutil.rmtree(os.path.join(root, item))