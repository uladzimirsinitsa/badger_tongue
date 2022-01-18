
import os
import sys

from dotenv import load_dotenv

load_dotenv()


PATH_START = os.environ['PATH_START']
PATH_END = os.environ['PATH_END']
DOMAIN = os.environ['DOMAIN']



def create_list_names() -> list | None:
    for _, _, names in os.walk(PATH_START):
        return names


def create_file(names: list) -> None:
    with open(f'{PATH_END}urls.csv', 'a') as file:
        for name in names:
            file.write(''.join((f'{DOMAIN}{name}', '\n')))


def main():
    names = create_list_names()
    create_file(names)
    sys.exit()


if __name__ == "__main__":
    main()
