
def count(str):
    dem = 0
    for char in str:
        dem+=1
    return(dem)

str= input('Nhập chuỗi: ')
print("Độ dài chuỗi là: ",count(str))
