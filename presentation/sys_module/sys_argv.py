import sys

for argv in sys.argv:
    print(argv)

for i in range(len(sys.argv)):
    print(sys.argv[i], ' [{}]'.format(i))

# cd presentation/sys_module
# python sys_argv.py first second ...
