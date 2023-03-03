# Input data: List of dictionaries
employee_list = [
   {"id": 12345, "name": "John", "department": "Kitchen"},
   {"id": 12456, "name": "Paul", "department": "House Floor"},
   {"id": 12478, "name": "Sarah", "department": "Management"},
   {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
   {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
   {"id": 12419, "name": "Gill", "department": "Cashier"}
]

# Function to be passed to the map() function. Do not change this.
def mod(employee_list):
   temp = employee_list['name'] + "_" + employee_list["department"]
   return temp

def to_mod_list(employee_list):
   ### WRITE SOLUTION CODE HERE
   list=map(mod,employee_list)
   return list
   raise NotImplementedError()

def generate_usernames(mod_list):
   ### WRITE SOLUTION CODE HERE
   list=map(mod,employee_list)
   list=[x.replace(" ","_") for x in list]
   return list
   raise NotImplementedError()

def map_id_to_initial(employee_list):
   ### WRITE SOLUTION CODE HERE
   f=[]
   d=[]
   for i in employee_list:
      n=i["name"]
      f.append(n[:1])
   for i in employee_list:
      n=i["id"]
      d.append(n)
   dict={key:value for (key,value) in zip(f,d)}
   return dict
   raise NotImplementedError()

def main():
   mod_emp_list = to_mod_list(employee_list)
   print("Modified employee list: " + str(mod_emp_list) + "\n")

   print(f"List of usernames: {generate_usernames(mod_emp_list)}\n")

   print(f"Initials and ids: {map_id_to_initial(employee_list)}")

if __name__ == "__main__":
   main()