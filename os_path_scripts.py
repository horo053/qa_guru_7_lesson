import os

CURRENT_FILE_PATH = os.path.abspath(__file__)
print(os.path.abspath(__file__))

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

print(os.path.dirname(CURRENT_FILE_PATH))
print(PROJECT_ROOT_PATH)

os.path.dirname(__file__)
print(os.path.dirname(__file__))
resources = os.path.join(PROJECT_ROOT_PATH, 'resources')
if not os.path.exists(resources):
    os.mkdir(resources)
print(resources)

resources = os.path.join(PROJECT_ROOT_PATH, '..', 'resources')
print(resources)
print(os.path.abspath(resources))
if not os.path.exists(resources):
    os.mkdir(resources)