import argparse, os, json, joblib, pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from features import make_synthetic
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--seed',type=int,default=42); ap.add_argument('--out',default='artifacts'); a=ap.parse_args()
    df=make_synthetic(seed=a.seed); X=df.drop(columns=['y']); y=df['y']
    Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=0.25,random_state=a.seed)
    pipe=Pipeline([('scaler',StandardScaler()),('clf',LogisticRegression(max_iter=1000))]).fit(Xtr,ytr)
    os.makedirs(a.out,exist_ok=True); X.to_parquet(os.path.join(a.out,'features.parquet')); joblib.dump(pipe,os.path.join(a.out,'model.pkl'))
    metrics={'train_score':float(pipe.score(Xtr,ytr)),'test_score':float(pipe.score(Xte,yte))}
    json.dump(metrics,open(os.path.join(a.out,'metrics.json'),'w'),indent=2)
if __name__=='__main__': main()
