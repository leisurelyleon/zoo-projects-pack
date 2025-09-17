import argparse,random,tempfile,os,subprocess
ap=argparse.ArgumentParser(); ap.add_argument('--iters',type=int,default=50); a=ap.parse_args()
for _ in range(a.iters):
    n=random.randint(1,20); s=['CADF v1']
    for _ in range(n): s.append(f"VERTEX {random.random():.3f} {random.random():.3f} {random.random():.3f}")
    for _ in range(max(0,n-2)): s.append(f"FACE {random.randint(0,n-1)} {random.randint(0,n-1)} {random.randint(0,n-1)}")
    with tempfile.NamedTemporaryFile('w',delete=False,suffix='.cadf') as tmp: tmp.write('\n'.join(s)+'\n'); path=tmp.name
    try: subprocess.run(['python','tools/validate.py',path],check=False)
    finally: os.unlink(path)
