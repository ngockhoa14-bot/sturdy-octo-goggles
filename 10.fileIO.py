FILE_NAME = "products.csv"

# đọc dữ liệu từ file và trả về danh sách đọc đc 
def read_products():
    # tạo 1 biến kiểu lít chứa tất cả các sản phẩm đọc đc từ file
    productlist = []
    
    try:
        with open(FILE_NAME, "r") as file:
            # bỏ qua dòng đầu 
            file.readline() 
            # đọc tiếp từ dòng thứ 2
            for line in file:
                line = line.strip()# strip bỏ ký tự \n ở cuối mỗi dòng

                # cắt chuỗi thành mãng
                data = line.split(",")
                # tạo sản phẩm theo dạng dictionary
                product = {
                    "id": data[0],
                    "name": data[1],
                    "price": data[2]
                }

                # thêm sản phẩm vào list
                productlist.append(product)
    except FileNotFoundError:
        print("File ko tìm thấy")
    except Exception as e:
        print("Erro:", e)


# Hàm hiển thị sản phẩm 
def display_product(products):
    #kiểm tra nêu file rỗng ( chưa có dữ liệu)
    if len(products) == 0:
        print("No produccts")
        return

    # nếu có dữ liệu thì in ra
    print("\n ----------- Producst List----------- ")
    for p in products:
        print(f"ProductID: {p['id']}  --- ProducName:{p['name']}   ---  Price:{p['price']}")
# Hàm thêm sản phẩm
def add_product(products):
    try:
        # Cho nhập product id
        product_id = input(" Enter product ID :")
        # Kiểm tra xem id này có tồn tại hay chưa
        for p in products:
            if p['id'].lower() == product_id.lower():
                print("ID Was duplicated")
                return
        # Nhập tiếp tên sản phẩm 
        products_name = input("Enter Product Name:")
        # Nhập giá sản phẩm
        product_price = float(input("Enter price:"))
        # Tạo sản phẩm dạng dictionary
        
        product = {"id": product_id, "name": products_name, "price": product_price}
        # Thêm sản phẩm vào danh sách
        products.append(product)
        print("Product added succesfully")
    except ValueError:
        print("price must be number")

# Hàm tìm kiếm sản phẩm
def search_product(products):
    # nhập id để tìm kiếm 
    product_id = input("Enter product ID:")

    # tạo 1 biến kiểu list để chứa các sản phẩm tìm thấy được
    found = []
    for p in products:
        if product_id in p['id'].lower():
            found.append(p)

    # kiểm tra xem có tìm kiếm được hay ko
    if len(found) > 0:
        display_product(found)
    else:
        print("No product found")

# Hàm lưu vào file
def save_product(products):
    try:
        with open(FILE_NAME, 'w') as file:
            # ghi lại dong đầu tiên
            file.write("ProductID,ProductName,Price\n")

            # ghi các dòng tiếp theo dựa vào danh sách
            for p in products:
                line = p['id'] + "," +p['name'] + "," + str(p['price']) + "\n"
                file.write(line)
                print("Write successfully")
    except Exception as e:
        print("Errou", e)


# Main Menu
def main():
    # đọc dữ liệu khi chương trình chạy, goi ham readproducts()
    products = read_products()
    while True:
        print("***************MENU***************")
        print("1. Display all products")
        print("2. All product")
        print("3. Seach product by id")
        print("4. Save product to file")
        print("5. Exit program")
        print("***************MENU***************")

        choice = input (" Enter your choice:")
        if choice == "1":
            display_product(products)
        elif choice =="2":
            add_product(products)
        elif choice =="3":
            search_product(products)
        elif choice =="4":
            save_product(products)
        elif choice =="5":
            print("Exit program")
            break
        else:
            print("Wrong choice. Enter 1-5")

# gọi hàm main
main()