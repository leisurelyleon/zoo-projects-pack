import argparse, os, json, joblib, pandas as pd
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--artifacts',required=True); a=ap.parse_args()
    m=joblib.load(os.path.join(a.artifacts,'model.pkl')); df=pd.read_parquet(os.path.join(a.artifacts,'features.parquet'))
    yhat=m.predict(df.drop(columns=['y'])); json.dump({'pred_sample_counts':int(yhat.shape[0])}, open(os.path.join(a.artifacts,'eval_summary.json'),'w'), indent=2)
    print('Wrote eval_summary.json')
if __name__=='__main__': main()
