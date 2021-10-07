import subprocess
import os
from pathlib import Path

global trackers, path

trackers_check = Path('trackers').exists()
trackers_empty = os.path.getsize('trackers')
path_check = Path('path').exists()
path_empty = os.path.getsize('path')

if trackers_check and path_check and trackers_empty != 0 and path_empty != 0:

    trackers = open('trackers')
    path = open('path').read()

    piece = input('Enter peace size [32kb, 64kb, 128kb, 256kb, 512kb, 1024(1mb), 2048(2mb),'
                  ' 4096(4mb), 8192(8mb), 16384(16mb)]: ')

    print('')

    if int(piece) in [32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]:

        if not Path('/home/user/upload/').is_dir():
            os.mkdir('/home/user/upload/')

        destination = '/home/user/upload/'

        for unit in trackers:
            temp = unit.split(' ')

            if not temp[0].strip() == 'none':
                tracker = '-t' + temp[0].strip()
            else:
                tracker = '-f'

            source = temp[1].strip('\n')

            ask = input('Create torrent for ' + source + '? (y/any): ')

            if ask == 'y':
                if not (Path(destination + source).is_dir()):
                    os.mkdir(destination + source)

                subprocess.run(['py3createtorrent', '-P', '-p' + piece, '-s' + source, tracker, path.strip(), '-o'
                                + destination + source])
            else:
                print(source + ' was skipped.')
            print('')
    else:
        print('Invalid piece size, aborted.')
    trackers.close()
else:
    if not trackers_check:
        print('Error: missing "trackers" file.')
    elif trackers_empty == 0:
        print('Error: "trackers" file is empty.')
    if not path_check:
        print('Error: missing "path" file.')
    elif path_empty == 0:
        print('Error: "path" file is empty.')
