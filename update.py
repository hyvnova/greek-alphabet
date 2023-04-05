import os

def get_dist():
	names = os.listdir("dist")
	versions = [*filter(lambda x: len(x) < 6 , [name.split("-")[1] for name in names])]
	
	d = dict(zip(versions,[int(x.replace(".","")) for x in versions]))

	version = max(d, key=d.get)
	
	return sorted([x for x in names if version in x])

def update_test():
    # create wheel
	os.system(f"python setup.py sdist bdist")
    
	dist = get_dist()
	os.system(f"twine upload --repository testpypi dist/{dist[1]}")

def update():
    # create wheel, para 
	os.system(f"python setup.py sdist bdist")
    
	dist = get_dist()
	os.system(f"twine upload dist/{dist[1]}")

update_test()
# Test Username : NoVa
# username : ezsnova
# update commands
# twine upload dist/ezstools-1.tar.gz dist/ezstools-1-py3-none-any.whl
# subir pypi test: twine upload --repository testpypi dist/{.tar} dist/{.whl}
