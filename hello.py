import sys
import multiprocesing as mp

print("Hello world!")
print("Python version %s " %str(sys.version))
print("Cores    %s " % mp.cpu_count())
