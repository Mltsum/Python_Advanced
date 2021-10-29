import os
import sys
import shutil

file_name = sys.argv[1]
print(f'当前文件需要修改为:{file_name}')

shutil.copy('/Users/mingren/Documents/07.Code/ScriptCrazyDevil/test/test.py', '.')
os.rename('./test.py', file_name)
