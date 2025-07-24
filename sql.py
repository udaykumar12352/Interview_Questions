class SQLTypeChecker:
    def _init_(self,schema):
        self.tables = schema
    def validate(self,query):
        query = query.lower().split()
        if query[0] != "select" or query[-1][-1] != ";":
            print("Invalid Starting or Ending")
            return
        cols = []
        tabls = []
        From = False
        Select = False
        for i in query:
            if i[-1] == ";":
                i = i [:-1]               
            if From:
                tabls.append(i)
                continue
            if i == "from" and not From:
                From = True
            if Select == True and not From:
                cols.append(i)
            if i == "select" and not Select:
                Select = True
            
        # Tables Query
        tabalias = {}
        more = False
        for i in tabls:
            if i[-1] == ",":
                more = True
                break
        if more and not "join" in tabls:
            tablsquery = " ".join(tabls).split(",")
            for i in tablsquery:
                jk = i.split()
                if jk[0] not in self.tables:
                    print(f"Table '{jk[0]}' doesn't exist")
                    return
                if len(jk) >1:
                    if jk[1] in tabalias:
                        print("Same Alias Declared")
                        return
                    tabalias[jk[1]] = jk[0]
                else :
                    tabalias[jk[0]] = jk[0]
        if not "join" in tabls and not more:
            if tabls[0] not in self.tables:
                print(f"Table '{i}' doesn't exist")
                return

        # Handling join operator
        if "join" in tabls:
            joinquery = " ".join(tabls).split("join")
            # Splitting join operation
            t1 = joinquery[0].split()
            joinquery2 = joinquery[1].split("on")
            #spliit
            t2 = joinquery2[0].split()
            eq = joinquery2[1]
            tabalias[t1[1]] = t1[0]
            tabalias[t2[1]] = t2[0]
            eq = eq.split("=")
            left = [eq[0].split(".")[0].strip() ,eq[0].split(".")[1].strip()]
            right = [eq[1].split(".")[0].strip() , eq[1].split(".")[1].strip()]
            if tabalias[t1[1]] not in self.tables or tabalias[t2[1]] not in self.tables :
                print("Tables not in the db")
                return
            if left[0] not in tabalias or right[0] not in tabalias:
                print("Alias Mismatch in equation", left,tabalias,right)
                return
            if left[1] not in self.tables[tabalias[left[0]]] or right[1] not in self.tables[tabalias[right[0]]]:
                print("columns in equation not exist")
                return
            if self.tables[tabalias[left[0]]][left[1]] != self.tables[tabalias[right[0]]][right[1]]:
                print(self.tables[tabalias[left[0]]][left[1]], self.tables[tabalias[right[0]]][right[1]])
                print("invalid operation on different column types")
                return
            print(joinquery)


        
        # Single alias
        if not more and len(tabls) >1 and "join" not in tabls:
            tabalias[tabls[1]] = tabls[0]

        # Sigle table without Alias
        if not more  and "join" not in tabls and len(tabls) == 1:
            tabalias[tabls[0]] = tabls[0]
            
        # Cols query
        dot = [True]
        alias = {}
        if len(tabls) > 1 or "." in " ".join(cols):
            for i in cols:
                if "." in i:
                    if i.split(".")[0] not in alias:
                        alias[i.split(".")[0]] = []
                    alias[i.split(".")[0]].append( i.split(".")[1])
                    dot.append(True)
                else:
                    if i != "*" :
                        dot.append(False)
            if not all(dot):
                print("invalid Usage of Alias or Abmigous Column exists in multiple tables")
                return

        # Column Validation
        if len(tabls) == 1:
            for i in cols:
                if i not in self.tables[tabls[0].lower()] and "." not in i and i != "*":
                    print(f"Column '{i}' not exist in '{tabls[0]}'")
                    return
                
        # Column Validation with alias
        for i,l in alias.items() :
            if i in tabalias:
                for k in l:
                    if k not in self.tables[tabalias[i]]:
                        print(f"Column '{k}' not exist in '{tabalias[i]}'")
                        return
            else :
                if i in list(tabalias.values()):
                    print("Mixed Table name and alias usage")
                    return
                print("Alias missmatch",tabalias)
                return
            
        print("Good")

from users import users as u
from orders import orders as o
from products import products as p
def main():
    schema = {"users" : u,
              "orders" : o,
              "products" : p
              }
    print(schema)
    
    sql = SQLTypeChecker (schema)
    # sql.validate()
    i = input("Enter Query to Validate: ")
    while i != "quit":
        sql.validate(i)
        i = input("Enter Query to Validate: ")
main()
