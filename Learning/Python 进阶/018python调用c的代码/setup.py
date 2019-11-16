from distutils.core import setup, Extension

swig_demo_module = Extension('_swig_demo',sources=['swig_demo_wrap.c', 'swig_demo.c'],)

setup(name='swig_demo',
      version='0.1',
      author="SWIG Docs",
      description="""Simple swig example from docs""",
      ext_modules=[swig_demo_module],
      py_modules=["swig_demo"],
      )
