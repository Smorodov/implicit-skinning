from pathlib import Path
import os

partnt_path=Path(__file__).parent.absolute()
includes=set()
sources=set()
headers=set()
for path in Path('OpenMesh').rglob('*.hh'):            
    headers.add(path.as_posix())    
    includes.add(os.path.dirname(path.as_posix()))

for path in Path('OpenMesh').rglob('*.cc'):            
    sources.add(path.as_posix())    

print('set( headers ')
for hdr in headers:
    print('"'+str(hdr)+'\"')
print(')\n')

print('set( sources ')
for src in sources:
    print('"'+str(src)+'\"')
print(')')

for inc in includes:
    print('inclide_directories(\"'+inc+'\")')