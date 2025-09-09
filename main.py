import hashlib
s='litebeta'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
