import ctypes
import os

# Load the native library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "libsic_native.so"))

# FFI function: malloc (ABI: C)
lib.malloc.argtypes = [ctypes.c_longlong]
lib.malloc.restype = None

# FFI function: free (ABI: C)
lib.free.argtypes = []
lib.free.restype = None

# FFI function: calloc (ABI: C)
lib.calloc.argtypes = [ctypes.c_longlong, ctypes.c_longlong]
lib.calloc.restype = None

# FFI function: realloc (ABI: C)
lib.realloc.argtypes = [ctypes.c_longlong]
lib.realloc.restype = None

# FFI function: printf (ABI: C)
lib.printf.argtypes = [ctypes.c_void_p]
lib.printf.restype = None

# FFI function: puts (ABI: C)
lib.puts.argtypes = [ctypes.c_void_p]
lib.puts.restype = None

# FFI function: putchar (ABI: C)
lib.putchar.argtypes = [ctypes.c_int]
lib.putchar.restype = None

# FFI function: fopen (ABI: C)
lib.fopen.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.fopen.restype = None

# FFI function: fclose (ABI: C)
lib.fclose.argtypes = [ctypes.c_void_p]
lib.fclose.restype = None

# FFI function: fread (ABI: C)
lib.fread.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
lib.fread.restype = None

# FFI function: fwrite (ABI: C)
lib.fwrite.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
lib.fwrite.restype = None

# FFI function: fprintf (ABI: C)
lib.fprintf.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.fprintf.restype = None

# FFI function: fgets (ABI: C)
lib.fgets.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]
lib.fgets.restype = None

# FFI function: fflush (ABI: C)
lib.fflush.argtypes = [ctypes.c_void_p]
lib.fflush.restype = None

# FFI function: malloc (ABI: C)
lib.malloc.argtypes = [ctypes.c_longlong]
lib.malloc.restype = None

# FFI function: free (ABI: C)
lib.free.argtypes = []
lib.free.restype = None

# FFI function: malloc (ABI: C)
lib.malloc.argtypes = [ctypes.c_longlong]
lib.malloc.restype = None

# FFI function: free (ABI: C)
lib.free.argtypes = []
lib.free.restype = None

# FFI function: realloc (ABI: C)
lib.realloc.argtypes = [ctypes.c_longlong]
lib.realloc.restype = None

# FFI function: sizeof (ABI: C)
lib.sizeof.argtypes = [ctypes.c_void_p]
lib.sizeof.restype = None

# FFI function: malloc (ABI: C)
lib.malloc.argtypes = [ctypes.c_longlong]
lib.malloc.restype = None

# FFI function: free (ABI: C)
lib.free.argtypes = []
lib.free.restype = None

# FFI function: realloc (ABI: C)
lib.realloc.argtypes = [ctypes.c_longlong]
lib.realloc.restype = None

# FFI function: strlen (ABI: C)
lib.strlen.argtypes = [ctypes.c_void_p]
lib.strlen.restype = None

# FFI function: memcpy (ABI: C)
lib.memcpy.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong]
lib.memcpy.restype = None

# FFI function: malloc (ABI: C)
lib.malloc.argtypes = [ctypes.c_longlong]
lib.malloc.restype = None

# FFI function: free (ABI: C)
lib.free.argtypes = []
lib.free.restype = None

# FFI function: realloc (ABI: C)
lib.realloc.argtypes = [ctypes.c_longlong]
lib.realloc.restype = None

# FFI function: memset (ABI: C)
lib.memset.argtypes = [ctypes.c_int, ctypes.c_longlong]
lib.memset.restype = None

# FFI function: fopen (ABI: C)
lib.fopen.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.fopen.restype = None

# FFI function: fclose (ABI: C)
lib.fclose.argtypes = [ctypes.c_void_p]
lib.fclose.restype = None

# FFI function: fread (ABI: C)
lib.fread.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
lib.fread.restype = None

# FFI function: fwrite (ABI: C)
lib.fwrite.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
lib.fwrite.restype = None

# FFI function: fseek (ABI: C)
lib.fseek.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
lib.fseek.restype = None

# FFI function: ftell (ABI: C)
lib.ftell.argtypes = [ctypes.c_void_p]
lib.ftell.restype = None

# FFI function: feof (ABI: C)
lib.feof.argtypes = [ctypes.c_void_p]
lib.feof.restype = None

# FFI function: ferror (ABI: C)
lib.ferror.argtypes = [ctypes.c_void_p]
lib.ferror.restype = None

# FFI function: malloc (ABI: C)
lib.malloc.argtypes = [ctypes.c_longlong]
lib.malloc.restype = None

# FFI function: free (ABI: C)
lib.free.argtypes = []
lib.free.restype = None

# FFI function: strcmp (ABI: C)
lib.strcmp.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.strcmp.restype = None

# FFI function: strlen (ABI: C)
lib.strlen.argtypes = [ctypes.c_void_p]
lib.strlen.restype = None

# FFI function: fgets (ABI: C)
lib.fgets.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]
lib.fgets.restype = None

# FFI function: feof (ABI: C)
lib.feof.argtypes = [ctypes.c_void_p]
lib.feof.restype = None

# FFI function: malloc (ABI: C)
lib.malloc.argtypes = [ctypes.c_longlong]
lib.malloc.restype = None

# FFI function: free (ABI: C)
lib.free.argtypes = []
lib.free.restype = None

# FFI function: memcpy (ABI: C)
lib.memcpy.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong]
lib.memcpy.restype = None

# FFI function: strstr (ABI: C)
lib.strstr.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.strstr.restype = None

# FFI function: strlen (ABI: C)
lib.strlen.argtypes = [ctypes.c_void_p]
lib.strlen.restype = None

# FFI function: printf (ABI: C)
lib.printf.argtypes = [ctypes.c_void_p]
lib.printf.restype = None

