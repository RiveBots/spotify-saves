"""
SETUP FILES On Python
"""
api = open('../api.sh', a)
api.write(f"python -M spotify-setup -A http://python.spoto.com/~/api/.data/spotify")
set = open('../setup.sh', a)
set.write(f"python -M spotify-setup")
