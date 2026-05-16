import sys
import traceback

def calculate_average(numbers):
    # Tinh tong cac phan tu trong danh sach
    total = sum(numbers)
    
    # Co tinh tao ra loi chia cho 0
    average = total / 0
    
    return average

def main():
    data = [10, 20, 30, 40]
    
    try:
        result = calculate_average(data)
        print(f"Ket qua trung binh: {result}")
    except Exception as e:
        # Su dung traceback de in ra toan bo chi tiet dong loi vao stderr
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()