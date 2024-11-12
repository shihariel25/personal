import pandas as pd
from string-grouper import group_string_similar

vendor = pd.read_csv(r"C:\Users\Documents\Sample\Vendor.csv")

vendor[["group-id", "Vendor_Name"]] = group_similar_strings(vendor["VendorName"], min_similarity=0.57)

vendor.to_csv(r"C:\Users\Documents\Sample\Vendor_New.csv")
