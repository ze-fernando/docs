import shutil

SOURCE_DIR = '/home/zeco/Code/study'
TARGET_DIR = './docs/'

def main():
    shutil.copytree(SOURCE_DIR, TARGET_DIR, ignore=shutil.ignore_patterns('.git', '.obsidian'), dirs_exist_ok=True)
    print('Finish')


main()
