def dis(price,rate):
    final_price = price * rate
    return final_price

old_price = float(input("请输入原价格："))
rate = float(input("请输入折扣率："))
new = dis(old_price,rate)
print('打折后的价格是：',new)
