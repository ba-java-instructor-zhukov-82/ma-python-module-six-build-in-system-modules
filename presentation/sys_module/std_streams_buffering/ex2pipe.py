import sys

var2 = sys.stdin.read()

print('Write to example_out.py standard out flow with print().')

sys.stdout.write(var2.upper())

# cd presentation/sys_module/std_streams_buffering
# python ex1pipe.py|python ex2pipe.py
#
# OUTPUT:
#
# Write to example_out.py standard out flow with print().
# WRITE TO STANDARD OUT FLOW SOME TEXT FROM EX1PIPE

