import pandas as pd
import os

# Read the large CSV
print("Reading CSV file...")
df = pd.read_csv('nypd_arrests_cleaned.csv')

total_rows = len(df)
print(f"Total rows: {total_rows}")

# Split into chunks (aim for ~200MB each, roughly 400k rows)
chunk_size = 400000

# Calculate number of chunks needed
num_chunks = (total_rows // chunk_size) + 1
print(f"Splitting into {num_chunks} chunks...")

# Create output directory
os.makedirs('data/processed/chunks', exist_ok=True)

# Split and save
for i in range(num_chunks):
    start_idx = i * chunk_size
    end_idx = min((i + 1) * chunk_size, total_rows)
    
    chunk = df[start_idx:end_idx]
    filename = f'data/processed/chunks/nypd_arrests_part_{i+1}.csv'
    
    chunk.to_csv(filename, index=False)
    print(f"Created {filename} with {len(chunk)} rows")

print("✅ Split complete!")