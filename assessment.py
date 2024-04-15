import pandas as pd

# Reading the CSV file into a pandas DataFrame
df = pd.read_csv("C:\\Users\\Lenovo\\Downloads\\Assignment1\\org_data.csv")

def get_managed_employees(employee_id, df):
    # Recursive function to find all managed employees
    def find_managed_employees(emp_id):
        # Find all employees who report to the given employee
        direct_reports = df[df['manager_id'] == emp_id]
        # Initializing a list to store managed employees
        managed_employees = [emp_id]
        # Iterating through direct reports recursively
        for idx, row in direct_reports.iterrows():
            managed_employees.extend(find_managed_employees(row['id']))
        return managed_employees
    
    # Finding all employees managed by the input employee
    managed_ids = find_managed_employees(employee_id)
    
    # Filtering the DataFrame to include only managed employees
    subset = df[df['id'].isin(managed_ids)]
    
    # Excluding the input employee from the output
    subset = subset[subset['id'] != employee_id]
    
    return subset


output1 = get_managed_employees(40, df)
print(output1)

output2 = get_managed_employees(10, df)
print(output2)


