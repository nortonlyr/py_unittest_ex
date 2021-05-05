# walk through
from mockito import when
import os

# stub 'os.path.exists'
when(os.path).exists('/foo').thenReturn(True)

os.path.exists('/foo')
# os.path.exists('/bar')