import argparse
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MySite.settings')
import django
django.setup()
from django.contrib.auth.models import User
from LoginScreen.models import ImageData
import shutil


if __name__ == '__main__':
    my_parser = argparse.ArgumentParser(description='DB populate params')
    my_parser.add_argument('data',
                           metavar='data',
                           type=str,
                           help='Path to Data Folder')

    my_parser.add_argument('username',
                           metavar='username',
                           type=str,
                           help='Database user')
    my_parser.add_argument("--dirs", nargs="+", default='all')
    args = my_parser.parse_args()

    dirs_to = args.dirs

    print(f'---------Adding {dirs_to} Files---------')
    data_path = args.data
    # csvs = os.listdir('media/CSV Files/')
    # pic = os.listdir('media/DB Pictures/')
    data = os.listdir(f'{data_path}/')
    us = User.objects.get(username=args.username)
    print('Adding Files in Database')
    for dirs in data:
        if dirs_to == 'all' or dirs in dirs_to:
            print(f'Reading Data from {dirs}')
            files = os.path.join(data_path, dirs)
            files_to_add = os.listdir(files)
            print('Adding Following Files')
            print(files_to_add, sep='\n')
            csv = [csv for csv in files_to_add if 'csv' in csv]
            if len(csv) > 0:
                csv = csv[0]
            else:
                csv = False
            for file in files_to_add:
                if 'csv' not in file:
                    if csv:

                        shutil.copyfile(os.path.join(data_path, dirs, csv), f'media/CSV Files/{csv}')
                        shutil.copyfile(os.path.join(data_path, dirs, file), f'media/DB Pictures/{file}')
                        obj = ImageData(user=us,
                                        title=dirs,
                                        description='',
                                        altText='',
                                        squareImage=f'DB Pictures/{file}',
                                        fileupload=f'CSV Files/{csv}',
                                        )
                        obj.save()
                    else:
                        shutil.copyfile(os.path.join(data_path, dirs, file), f'media/DB Pictures/{file}')
                        obj = ImageData(user=us,
                                        title=dirs,
                                        description='',
                                        altText='',
                                        squareImage=f'DB Pictures/{file}'
                                        )
                        obj.fileupload = None
                        obj.save()
    print('Files Successfully Added to Database.')
