import sys

def calculate_average(numbers):
    # Tinh tong cac phan tu trong danh sach
    total = sum(numbers)
    
    # Co tinh tao ra loi chia cho 0 de he thong bat duoc log
    # AI se phai doc log, phan tich va sua thanh: total / len(numbers)
    average = total / 0
    
    return average

def main():
    # Khoi tao danh sach du lieu mau
    data = [10, 20, 30, 40]
    
    try:
        result = calculate_average(data)
        # In ket qua neu chay thanh cong
        print(f"Ket qua trung binh: {result}")
    except Exception as e:
        # Ban ma loi ra stderr kem exit code 1 de Docker ghi nhan that bai
        print(f"ZeroDivisionError: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()