import sys,json
def parse(lines):
    assert lines[0].strip()=="CADF v1","bad header"
    V,F=[],[]
    for ln in lines[1:]:
        ln=ln.strip()
        if not ln: continue
        t,*r=ln.split()
        if t=="VERTEX": x,y,z=map(float,r); V.append([x,y,z])
        elif t=="FACE": i,j,k=map(int,r); F.append([i,j,k])
    return {"vertices":V,"faces":F}
if __name__=="__main__":
    with open(sys.argv[1],"r",encoding="utf-8") as f:
        obj=parse(f.readlines())
    json.dump(obj,sys.stdout,indent=2)
