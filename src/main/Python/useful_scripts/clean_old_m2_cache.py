import re
import shutil
from os import listdir
from os.path import isdir

dry_run = False  # change to True to get a log of what will be removed
m2_path = '/Users/ronnen/.m2/repository/'  # here comes your repo path
version_regex = '^\d[.\d]*$'


def check_and_clean(path):
    files = listdir(path)
    for file in files:
        if not isdir('/'.join([path, file])):
            return
    last = check_if_versions(files)
    if last is None:
        for file in files:
            check_and_clean('/'.join([path, file]))
    elif len(files) == 1:
        return
    else:
        print('update ' + path.split(m2_path)[1])
        for file in files:
            if file == last:
                continue
            print(file + ' (newer version: ' + last + ')')
            if not dry_run:
                shutil.rmtree('/'.join([path, file]))


def check_if_versions(files):
    if len(files) == 0:
        return None
    last = ''
    for file in files:
        if re.match(version_regex, file):
            if last == '':
                last = file
            if len(last.split('.')) == len(file.split('.')):
                for (current, new) in zip(last.split('.'), file.split('.')):
                    if int(new) > int(current):
                        last = file
                        break
                    elif int(new) < int(current):
                        break
            else:
                return None
        else:
            return None
    return last


check_and_clean(m2_path)
