# a
import glob
import ast
import shlex
import subprocess
import os
import pandas as pd

path = 'C:/Users/neo qi xiang/Desktop/coding challenge/*.py'

def get_pyfiles(pat):
    py_files = glob.glob(path, recursive=True)
    return py_files

def get_comment_code(files):
    code = 0 # example inline comment
    comments = 0
    file_comment_count = []
    file_code_count  = []
    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()
        for line in lines:
            if line.strip().startswith('#'):
                comments += 1
            else:
                code += 1
        file_comment_count.append(comments)
        file_code_count.append(code)
    
    print(f'filenme: {file} :\nlines of code: {code}\nlines of comments: {comments}')
    print(file_code_count)
    return file_comment_count, file_code_count


class CountFunc(ast.NodeVisitor):
    func_count = 0
    def visit_ClassDef(self, node):
        return
    def visit_FunctionDef(self, node):
        self.func_count += 1
    def visit_Lambda(self, node):
        self.func_count += 1

def get_function(files):
    functions = 0
    file_function = []
    for file in files:
        p = ast.parse(open(file).read())
        f = CountFunc()
        f.visit(p)
        functions += f.func_count
        print(f'for file {files}: \n total functions defined: {functions}')
        file_function.append(functions)
    return file_function


def create_stats(path_target):
    py_files = get_pyfiles(path_target)
    comments, code = get_comment_code(py_files)
    functions = get_function(py_files)
    stats = pd.DataFrame(list(zip(py_files, comments, code, functions )),
              columns=['path','number_comments', 'number_code','number_function'])
    return stats

statistics = create_stats(path)

print(statistics)





""""
cmd = 'git diff --shortstat HEAD HEAD-3' 
cmd = shlex.split(cmd)
p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
out, _ = p.communicate()
print(f'number of lines changed: {out}')

cmd = os.chdir('cd ~/my-python-project; du -h --max-depth=2 -m')
cmd = shlex.split(cmd)
p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
out, _ = p.communicate()
print(f'folder size per each subfolder in MB:\n{out}')

"""