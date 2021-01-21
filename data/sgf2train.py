import os


def get_sgf(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.sgf')]


sgf_path = get_sgf('./sgf_record')
print(sgf_path)
