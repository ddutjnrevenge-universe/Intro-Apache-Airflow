import yfinance as yf
import pickle

tsla = yf.Ticker("TSLA")
print(tsla)
rec = tsla.recommendations
print(rec)
def get_recommendation(row):
    if row['buy'] > row['sell'] and row['buy'] > row['hold']:
        return 'Buy'
    elif row['sell'] > row['buy'] and row['sell'] > row['hold']:
        return 'Sell'
    else:
        return 'Hold'

# Apply the function to each row
rec['To Grade'] = rec.apply(get_recommendation, axis=1)
# 1st Reco
print(tsla.recommendations["To Grade"].value_counts().keys()[0])
# 2nd Reco (commented out for now)
print(tsla.recommendations["To Grade"].value_counts().keys()[1])
# Check if recommendations exist and contain the expected data
# if tsla.recommendations is not None and "To Grade" in tsla.recommendations.columns:
#     # 1st Reco
#     print(tsla.recommendations["To Grade"].value_counts().keys()[0])
#     # 2nd Reco (commented out for now)
#     print(tsla.recommendations["To Grade"].value_counts().keys()[1])
# else:
#     print("No recommendations data available or 'To Grade' column is missing.")

# Save the recommendations to a file (commented out for now)
with open('/tmp/script.out', 'wb+') as tmp_file:
   pickle.dump({'test': 'ok'}, tmp_file)
