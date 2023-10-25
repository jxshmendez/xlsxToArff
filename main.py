import pandas as pd

# Read Excel data into a DataFrame
data = pd.read_excel(".xlsx")#add path to xlsx you want to convert

# Define attribute names and types
attributes = [
#Add attributes here
#example heading name then type ('Case_no', 'numeric'),
]

arff_file_path = ".arff" #select file save path
with open(arff_file_path, "w") as arff_file:
    arff_file.write("@relation \n\n")#arff needs relation name, add it after '@relation'

    # Write attribute definitions
    for attr_name, attr_type in attributes:
        arff_file.write(f"@attribute {attr_name} {attr_type}\n")

    arff_file.write("\n@data\n")

    # Write data rows
    for index, row in data.iterrows():

        values = ",".join(f"'{row[attr_name]}'" if attr_type == 'string' else str(row[attr_name]) for attr_name, attr_type in attributes)
        arff_file.write(f"{values}\n")

print(f"ARFF file saved to {arff_file_path}")
