import pandas as pd
import re

# Input and Output file paths
input_file = "pfam_results.txt"  # Change this to the actual filename
output_file = "pfam_results.csv"

# Read the file and filter out comment lines
with open(input_file, "r") as f:
    lines = f.readlines()

# Remove comment lines (starting with "#")
filtered_lines = [line.strip() for line in lines if not line.startswith("#") and line.strip()]

# Extract relevant columns
data = []
for line in filtered_lines:
    columns = re.split(r"\s+", line)  # Split by whitespace
    if len(columns) >= 8:  # Ensure it has at least 8 columns
        target_name = columns[0]  # Pfam domain name
        accession = columns[1]  # Pfam accession number
        tlen = columns[2]  # Target length
        query_name = columns[3]  # Query sequence name
        qlen = columns[5]  # Query sequence length
        e_value = columns[6]  # E-value
        score = columns[7]  # Score
        bias = columns[8] if len(columns) > 8 else "NA"  # Bias score (handle missing values)
        
        data.append([target_name, accession, tlen, query_name, qlen, e_value, score, bias])

# Define column names
columns = ["Target Name", "Accession", "Target Length", "Query Name", "Query Length", "E-value", "Score", "Bias"]

# Convert to DataFrame
df = pd.DataFrame(data, columns=columns)

# Save as CSV
df.to_csv(output_file, index=False)

print(f"CSV file saved as {output_file}")
