# encoding: utf-8
# module psutil._psutil_linux calls itself psutil_linux
# from /home/fred/.local/lib/python3.4/site-packages/psutil/_psutil_linux.cpython-34m.so
# by generator 1.136
# no doc
# no imports

# Variables with simple values

DUPLEX_FULL = 1
DUPLEX_HALF = 0
DUPLEX_UNKNOWN = 255

RLIMIT_AS = 9
RLIMIT_CORE = 4
RLIMIT_CPU = 0
RLIMIT_DATA = 2
RLIMIT_FSIZE = 1
RLIMIT_LOCKS = 10
RLIMIT_MEMLOCK = 8
RLIMIT_MSGQUEUE = 12
RLIMIT_NICE = 13
RLIMIT_NOFILE = 7
RLIMIT_NPROC = 6
RLIMIT_RSS = 5
RLIMIT_RTPRIO = 14
RLIMIT_RTTIME = 15
RLIMIT_SIGPENDING = 11
RLIMIT_STACK = 3

RLIM_INFINITY = -1

version = 322

# functions

def disk_partitions(*args, **kwargs): # real signature unknown
    """ Return disk mounted partitions as a list of tuples including device, mount point and filesystem type """
    pass

def linux_prlimit(*args, **kwargs): # real signature unknown
    """ Get or set process resource limits. """
    pass

def linux_sysinfo(*args, **kwargs): # real signature unknown
    """ A wrapper around sysinfo(), return system memory usage statistics """
    pass

def net_if_stats(*args, **kwargs): # real signature unknown
    """ Return NIC stats (isup, duplex, speed, mtu) """
    pass

def proc_cpu_affinity_get(*args, **kwargs): # real signature unknown
    """ Return process CPU affinity as a Python long (the bitmask). """
    pass

def proc_cpu_affinity_set(*args, **kwargs): # real signature unknown
    """ Set process CPU affinity; expects a bitmask. """
    pass

def proc_ioprio_get(*args, **kwargs): # real signature unknown
    """ Get process I/O priority """
    pass

def proc_ioprio_set(*args, **kwargs): # real signature unknown
    """ Set process I/O priority """
    pass

def users(*args, **kwargs): # real signature unknown
    """ Return currently connected users as a list of tuples """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

