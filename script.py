from cx_Freeze import setup, Executable

setup(name='nome-do-arquivo',
      version='1.0',
      description='descrição do programa',
      options={'build_exe': {'packages': ['matplotlib']}},
      executables=[Executable(
          script='script.py',
          base=None
          icon = 'my-icon.ico'
)
]
)