import argparse, csv, hashlib, json, os
from datetime import datetime

def sha256_of(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for ch in iter(lambda:f.read(65536),b''): h.update(ch)
    return h.hexdigest()

def normalize(rec, src):
    def g(k,d=None): 
        return rec[k] if k in rec and rec[k] not in ("",None) else d
    bbox = g('bbox', {'x':0,'y':0,'z':0})
    return [str(g('part_id','unknown')), str(g('assembly','main')), str(g('version','v1')),
            str(g('updated_at', datetime.utcnow().isoformat())), str(g('material','unspecified')),
            float(g('mass_kg',0.0)), float(bbox.get('x',0)), float(bbox.get('y',0)), float(bbox.get('z',0)),
            sha256_of(src), os.path.basename(src)]

def load_json(p): 
    x=json.load(open(p)); return x if isinstance(x,list) else [x]

def load_csv(p):
    out=[]
    with open(p,encoding='utf-8') as f:
        for r in csv.DictReader(f):
            out.append({'part_id':r.get('part_id'),'assembly':r.get('assembly'),'version':r.get('version'),
                        'updated_at':r.get('updated_at'),'material':r.get('material'),
                        'mass_kg':float(r.get('mass_kg',0) or 0),
                        'bbox':{'x':float(r.get('bbox_x',0) or 0),'y':float(r.get('bbox_y',0) or 0),'z':float(r.get('bbox_z',0) or 0)}})
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input',required=True); ap.add_argument('--output',required=True)
    a=ap.parse_args(); rows=[]; hdr=['part_id','assembly','version','updated_at','material','mass_kg','bbox_x','bbox_y','bbox_z','checksum','source_file']
    for root,_,files in os.walk(a.input):
        for fn in files:
            p=os.path.join(root,fn)
            if fn.lower().endswith('.json'): recs=load_json(p)
            elif fn.lower().endswith('.csv'): recs=load_csv(p)
            else: continue
            for r in recs: rows.append(normalize(r,p))
    os.makedirs(os.path.dirname(a.output),exist_ok=True)
    with open(a.output,'w',newline='',encoding='utf-8') as f:
        w=csv.writer(f); w.writerow(hdr); w.writerows(rows)

if __name__=='__main__': main()
