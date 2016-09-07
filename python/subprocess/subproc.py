import subprocess

print('ls output: ')
subprocess.call('ls')
print()

print('ls -l output: ')
subprocess.call(['ls', '-l'])
print()

output = subprocess.check_output(['ls', '-l'])
print("ls -l using check_output: {}".format(output))
print('type of output is : {}'.format(type(output)))
print()

output = subprocess.check_output(['ls -l *py'], shell=True)
print('output using wildcard: {}'.format(output))
print()
