import telegram_message
import pandas as pd


url = 'https://docs.google.com/spreadsheets/d/1D4H2OoHOFVPmCoyKBVCjxIl0Bt3RLYSz/gviz/tq?tqx=out:csv&sheet=Champions'
df = pd.read_csv(url)
df = df.iloc[:,[0, 1, 19, 22, 23, -1]]
df = df.iloc[2:]
df = df[df.iloc[:, 2] >= 4]
print(df.head(4))

df_buy = df[df.iloc[:, 3].str.contains("Above Fair Value") == False]
print(df_buy)

df_sell = df[df.iloc[:, 3].str.contains("Above Fair Value") == True]
print(df_sell)

telegram_message.send_message("kagi")



