n = int(input()) #nhập giá trị n từ bàn phím  # 1 phép gán
sum = 0 # biến lưu kết quả                      # 1 phép gán
for i in range(1,n+1): #i sẽ chạy từ 1 đến n    # n phép +
    sum += i                                    # n phép + và n phép gán
print(sum)                          
# số lượng phép toán là một hàm phụ thuộc n --> O(3n+2) = O(n)

print(sum*2)
