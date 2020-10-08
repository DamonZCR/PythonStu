"""将文件gx对话.txt中的数据分割：
-顾客的对话单独保存为cus_*.txt文件（每句去除‘顾客：’）
-卖家的对话单独保存为shop_*.txt文件（每句去除‘卖家：’）
-以‘====...’为分割，分为三段。每一段可分为以上两个文件
共六个文件。"""

f = open('d:/gx对话.txt',encoding = 'UTF-8')
cus = list()
shop = list()
count = 1

for each_line in f:
    if each_line[:6] != '======':
        (front , behind) = each_line.split('：',1)
        if  '顾客' in front:
            cus.append(behind)
        elif '老板' in front:
            shop.append(behind)
    else:
        cus_file_name = 'd:/cus_'+str(count)+'.txt'
        shop_file_name = 'd:/shop_'+str(count)+'.txt'

        cus_file = open(cus_file_name , 'w')
        shop_file = open(shop_file_name , 'w')
        cus_file.writelines(cus)
        shop_file.writelines(shop)

        cus_file.close()
        shop_file.close()
        count += 1


#最后一个文件执行文件保存
cus_file_name = 'd:/cus_'+str(count)+'.txt'
shop_file_name = 'd:/shop_'+str(count)+'.txt'

cus_file = open(cus_file_name , 'w')
shop_file = open(shop_file_name , 'w')
cus_file.writelines(cus)
shop_file.writelines(shop)

cus_file.close()
shop_file.close()
        
f.close()

        
