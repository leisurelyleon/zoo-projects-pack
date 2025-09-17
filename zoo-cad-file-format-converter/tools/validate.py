import sys,hashlib
p=sys.argv[1]
h=hashlib.sha256(open(p,'rb').read()).hexdigest()
print("OK checksum="+h) if open(p).readline().strip()=="CADF v1" else print("Invalid header")
