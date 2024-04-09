from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Column 1","Column 2","Column 3"]
table.add_row(["eh",45,123.8])
print(table)
