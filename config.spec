# -*- mode: python ; coding: utf-8 -*-
import sys
sys.setrecursionlimit(1000000)
block_cipher = None


a = Analysis(['config.py', 'Data.py', 'Device.py', 'dl_gui.py', 'getmakpolygon.py', 'main_gui.py', 'main_logic.py', 'model.py', 'parallel_model.py', 'robot.py', 'robot_logic.py', 'stopThreading.py', 'trans.py', 'utils.py', 'visualize.py'],
             pathex=['C:\\anaconda\\envs\\simple\\Lib\\site-packages', 'C:\\dl_gui_v1.0_打包'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['hooks'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='config',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='config')
