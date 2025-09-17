import numpy as np, pandas as pd
def make_synthetic(n=5000, seed=42):
    rng=np.random.default_rng(seed)
    x1=rng.normal(0,1,n); x2=rng.normal(2,0.5,n); x3=rng.uniform(-1,1,n)
    y=((x1+0.7*x2-0.3*x3+rng.normal(0,0.5,n))>1.0).astype(int)
    df=pd.DataFrame({'x1':x1,'x2':x2,'x3':x3,'y':y})
    df['x1_x2']=df['x1']*df['x2']; df['x2_sq']=df['x2']**2
    return df
