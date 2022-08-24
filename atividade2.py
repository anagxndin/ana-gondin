import mysql.connector

mydb = mysql.connector.connect(
    host = "relational.fit.cvut.cz",
    user = "guest",
    password = "relational",
    database = "northwind"
)

print("----- TABELAS NORTHWIND ----- \n")
print("1 - Categories")
print("2 - CustomerCustomerDemo")
print("3 - CustomerDemographics")
print("4 - Customers")
print("5 - EmployeeTerritories")
print("6 - Employees")
print("7 - Order Details")
print("8 - Orders")
print("9 - Products")
print("10 - Region")
print("11 - Shippers")
print("12 - Suppliers")
print("13 - Territories")
ntabela = input("\n Escolha uma tabela a ser consultada: ")

if (ntabela == '1'):
    tabela = "Categories"
    print("----- COLUNAS DE 'CATEGORIES' ----- \n")
    print("1 - CategoryID")
    print("2 - CategoryName")
    print("3 - Description")
    print("4 - Picture")
    ncoluna = input("Escolha uma coluna da tabela Categories: ")
    if (ncoluna == '1'):
        coluna = "CategoryID"
    elif (ncoluna == '2'):
        coluna = "CategoryName"
    elif (ncoluna == '3'):
        coluna = "Description"
    elif (ncoluna == '4'):
        coluna = "Picture"
    

    

elif (ntabela == '2'):
    tabela = "CustomerCustomerDemo"
    print("----- COLUNAS DE 'CUSTOMERCUSTOMERDEMO' ----- \n")
    print("1 - CustomerID")
    print("2 - CustomerTypeID")
    ncoluna = input("Escolha uma coluna da tabela CustomerCustomerDemo: ")
    if (ncoluna == '1'):
        coluna = "CustomerID"
    elif (ncoluna == '2'):
        coluna = "CustomerTypeID"
    


elif (ntabela == '3'):
    tabela = "CustomerDemographics"
    print("----- COLUNAS DE 'CustomerDemographics' ----- \n")
    print("1 - CustomerTypeID")
    print("2 - CustomerDesc")
    ncoluna = input("Escolha uma coluna da tabela CustomerDemographics: ")
    if (ncoluna == '1'):
        coluna = "CustomerTypeID"
    elif (ncoluna == '2'):
        coluna = "CustomerDesc"
    



elif (ntabela == '4'):
    tabela = "Customers"
    print("----- COLUNAS DE 'Customers' ----- \n")
    print("1 - CustomerID")
    print("2 - CompanyName")
    print("3 - ContactName")
    print("4 - ContactTitle")
    print("5 - Address")
    print("6 - City")
    print("7 - Region")
    print("8 - PostalCode")
    print("9 - Country")
    print("10 - Phone")
    print("11 - Fax")
    ncoluna = input("Escolha uma coluna da tabela Customers: ")
    if (ncoluna == '1'):
        coluna = "CustomerID"
    elif (ncoluna == '2'):
        coluna = "CompanyName"
    elif (ncoluna == '3'):
        coluna = "ContactName"
    elif (ncoluna == '4'):
        coluna = "ContactTitle"
    elif (ncoluna == '5'):
        coluna = "Address"
    elif (ncoluna == '6'):
        coluna = "City"
    elif (ncoluna == '7'):
        coluna = "Region"
    elif (ncoluna == '8'):
        coluna = "PostalCode"
    elif (ncoluna == '9'):
        coluna = "Country"
    elif (ncoluna == '10'):
        coluna = "Phone"
    elif (ncoluna == '11'):
        coluna = "Fax"


elif (ntabela == '5'):
    tabela = "EmployeeTerritories"
    print("----- COLUNAS DE 'EmployeeTerritories' ----- \n")
    print("1 - EmployeeID")
    print("2 - TerritoryID")
    ncoluna = input("Escolha uma coluna da tabela EmployeeTerritories: ")
    if (ncoluna == '1'):
        coluna = "EmployeeID"
    elif (ncoluna == '2'):
        coluna = "TerritoryID"


elif (ntabela == '6'):
    tabela = "Employees"
    print("----- COLUNAS DE 'Employees' ----- \n")
    print("1 - EmployeeID")
    print("2 - LastName")
    print("3 - FirstName")
    print("4 - Title")
    print("5 - TitleOfCourtesy")
    print("6 - BirthDate")
    print("7 - HireDate")
    print("8 - Address")
    print("9 - City")
    print("10 - Region")
    print("11 - PostalCode")
    print("12 - Country")
    print("13 - HomePhone")
    print("14 - Extension")
    print("15 - Photo")
    print("16 - Notes")
    print("17 - ReportsTo")
    print("18 - PhotoPath")
    print("19 - Salary")
    ncoluna = input("Escolha uma coluna da tabela Employees: ")
    if (ncoluna == '1'):
        coluna = "EmployeeID"
    elif (ncoluna == '2'):
        coluna = "LastName"
    elif (ncoluna == '3'):
        coluna = "FirstName"
    elif (ncoluna == '4'):
        coluna = "Title"
    elif (ncoluna == '5'):
        coluna = "TitleOfCourtesy"
    elif (ncoluna == '6'):
        coluna = "BirthDate"
    elif (ncoluna == '7'):
        coluna = "HireDate"
    elif (ncoluna == '8'):
        coluna = "Address"
    elif (ncoluna == '9'):
        coluna = "City"
    elif (ncoluna == '10'):
        coluna = "Region"
    elif (ncoluna == '11'):
        coluna = "PostalCode"
    elif (ncoluna == '12'):
        coluna = "Country"
    elif (ncoluna == '13'):
        coluna = "HomePhone"
    elif (ncoluna == '14'):
        coluna = "Extension"
    elif (ncoluna == '15'):
        coluna = "Photo"
    elif (ncoluna == '16'):
        coluna = "Notes"
    elif (ncoluna == '17'):
        coluna = "ReportsTo"
    elif (ncoluna == '18'):
        coluna = "PhotoPath"
    elif (ncoluna == '19'):
        coluna = "Salary"


elif (ntabela == '7'):
    tabela = "Order Details"
    print("----- COLUNAS DE 'Order Details' ----- \n")
    print("1 - OrderID")
    print("2 - ProductID")
    print("3 - UnitPrice")
    print("4 - Quantity")
    print("5 - Discount")
    ncoluna = input("Escolha uma coluna da tabela Order Details: ")
    if (ncoluna == '1'):
        coluna = "OrderID"
    elif (ncoluna == '2'):
        coluna = "ProductID"
    elif (ncoluna == '3'):
        coluna = "UnitPrice"
    elif (ncoluna == '4'):
        coluna = "Quantity"
    elif (ncoluna == '5'):
        coluna = "Discount"

elif (ntabela == '8'):
    tabela = "Orders"
    print("----- COLUNAS DE 'Orders' ----- \n")
    print("1 - OrderID")
    print("2 - CustomerID")
    print("3 - EmployeeID")
    print("4 - OrderDate")
    print("5 - RequiredDate")
    print("6 - ShippedDate")
    print("7 - ShipVia")
    print("8 - Freight")
    print("9 - ShipName")
    print("10 - ShipAddress")
    print("11 - ShipCity")
    print("12 - ShipRegion")
    print("13 - ShipPostalCode")
    print("14 - ShipCountry")
    ncoluna = input("Escolha uma coluna da tabela Orders: ")
    if (ncoluna == '1'):
        coluna = "OrderID"
    elif (ncoluna == '2'):
        coluna = "CustomerID"
    elif (ncoluna == '3'):
        coluna = "EmployeeID"
    elif (ncoluna == '4'):
        coluna = "OrderDate"
    elif (ncoluna == '5'):
        coluna = "RequiredDate"
    elif (ncoluna == '6'):
        coluna = "ShippedDate"
    elif (ncoluna == '7'):
        coluna = "ShipVia"
    elif (ncoluna == '8'):
        coluna = "Freight"
    elif (ncoluna == '9'):
        coluna = "ShipName"
    elif (ncoluna == '10'):
        coluna = "ShipAddress"
    elif (ncoluna == '11'):
        coluna = "ShipCity"
    elif (ncoluna == '12'):
        coluna = "ShipRegion"
    elif (ncoluna == '13'):
        coluna = "ShipPostalCode"
    elif (ncoluna == '14'):
        coluna = "ShipCountry"


elif (ntabela == '9'):
    tabela = "Products"
    print("----- COLUNAS DE 'Products' ----- \n")
    print("1 - ProductID")
    print("2 - ProductName")
    print("3 - SupplierID")
    print("4 - CategoryID")
    print("5 - QuantityPerUnit")
    print("6 - UnitPrice")
    print("7 - UnitsInStock")
    print("8 - UnitsOnOrder")
    print("9 - ReorderLevel")
    print("10 - Discontinued")
    ncoluna = input("Escolha uma coluna da tabela Products: ")
    if (ncoluna == '1'):
        coluna = "ProductID"
    elif (ncoluna == '2'):
        coluna = "ProductName"
    elif (ncoluna == '3'):
        coluna = "SupplierID"
    elif (ncoluna == '4'):
        coluna = "CategoryID"
    elif (ncoluna == '5'):
        coluna = "QuantityPerUnit"
    elif (ncoluna == '6'):
        coluna = "UnitPrice"
    elif (ncoluna == '7'):
        coluna = "UnitsInStock"
    elif (ncoluna == '8'):
        coluna = "UnitsOnOrder"
    elif (ncoluna == '9'):
        coluna = "ReorderLevel"
    elif (ncoluna == '10'):
        coluna = "Discontinued"

elif (ntabela == '10'):
    tabela = "Region"
    print("----- COLUNAS DE 'Region' ----- \n")
    print("1 - RegionID")
    print("2 - RegionDescription")
    ncoluna = input("Escolha uma coluna da tabela Region")
    if (ncoluna == '1'):
        coluna = "RegionID"
    elif (ncoluna == '2'):
        coluna = "RegionDescription"

elif (ntabela == '11'):
    tabela = "Shippers"
    print("----- COLUNAS DE 'Shippers' ----- \n")
    print("1 - ShipperID")
    print("2 - CompanyName")
    print("3 - Phone")
    ncoluna = input("Escolha uma coluna da tabela Shippers: ")
    if (ncoluna == '1'):
        coluna = "ShipperID"
    elif (ncoluna == '2'):
        coluna = "CompanyName"
    elif (ncoluna == '3'):
        coluna = "Phone"

elif (ntabela == '12'):
    tabela = "Suppliers"
    print("----- COLUNAS DE 'Suppliers' ----- \n")
    print("1 - SupplierID")
    print("2 - CompanyName")
    print("3 - ContactName")
    print("4 - ContactTitle")
    print("5 - Address")
    print("6 - City")
    print("7 - Region")
    print("8 - PostalCode")
    print("9 - Country")
    print("10 - Phone")
    print("11 - Fax")
    print("12 - HomePage")
    ncoluna = input("Escolha uma coluna da tabela Suppliers: ")
    if (ncoluna == '1'):
        coluna = "SupplierID"
    elif (ncoluna == '2'):
        coluna = "CompanyName"
    elif (ncoluna == '3'):
        coluna = "ContactName"
    elif (ncoluna == '4'):
        coluna = "ContactTitle"
    elif (ncoluna == '5'):
        coluna = "Address"
    elif (ncoluna == '6'):
        coluna = "City"
    elif (ncoluna == '7'):
        coluna = "Region"
    elif (ncoluna == '8'):
        coluna = "PostalCode"
    elif (ncoluna == '9'):
        coluna = "Country"
    elif (ncoluna == '10'):
        coluna = "Phone"
    elif (ncoluna == '11'):
        coluna = "Fax"
    elif (ncoluna == '12'):
        coluna = "HomePage"

elif (ntabela == '13'):
    tabela = "Territories"
    print("----- COLUNAS DE 'Territories' ----- \n")
    print("1 - TerritoryID")
    print("2 - TerritoryDescription")
    print("3 - RegionID")
    ncoluna = input("Escolha uma coluna da tabela Territories")
    if (ncoluna == '1'):
        coluna = "TerritoryID"
    elif (ncoluna == '2'):
        coluna = "TerritoryDescription"
    elif (ncoluna == '3'):
        coluna = "RegionID" 

consulta = input("Digite o conteúdo que deseja pesquisar: ")

mycursor = mydb.cursor()

mycursor.execute(f'select * from {tabela} where {coluna} like "%{consulta}%"')

myresult = mycursor.fetchall()
print("\n Resultados da sua consulta: ")
for registro in myresult:
    print(registro)

