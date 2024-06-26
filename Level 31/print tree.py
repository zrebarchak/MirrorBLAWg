import os

def print_tree(startpath, prefix=''):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * level
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
    print_tree(base_dir)
