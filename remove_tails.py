import os

if __name__ == '__main__':
    folder = 'D:\\math\\LinAlg'
    files = [f for f in os.listdir(folder) if f.endswith('.mp4')]

    for file in files:
        fullpath = os.path.join(folder, file)
        new_name = fullpath.replace(' - YouTube', '')
        os.rename(fullpath, new_name)

        print(file)

