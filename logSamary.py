import pandas as pd

log = pd.read_csv('エラーメッセージ履歴_YYYYMMDD-01作成.txt',  delimiter='\t', encoding="SHIFT-JIS")
print(log.head())