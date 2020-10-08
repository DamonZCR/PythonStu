import pickle

def make_file(cus ,shop ,count):
    cus_file_name = 'd:/cus_'+str(count)+'.txt'
    shop_file_name = 'd:/shop_'+str(count)+'.txt'

    cus_file = open(cus_file_name , 'wb')
    shop_file = open(shop_file_name , 'wb')
    pickle.dump(cus, cus_file)
    pickle.dump(shop, shop_file)

    cus_file.close()
    shop_file.close()
    
def main_make_file(filename):
    f = open(filename, encoding = 'UTF-8')
    cus = list()
    shop = list()
    count = 1

    for each_line in f:
        if each_line[:6] != '======':
            if each_line != '\n':
                (front , behind) = each_line.split('：',1)
                if  '顾客' in front:
                    cus.append(behind)
                elif '老板' in front:
                    shop.append(behind)
        else:
            make_file(cus ,shop ,count)
            count += 1


    #最后一个文件执行文件保存
    make_file(cus ,shop ,count)
            
    f.close()
main_make_file('d:/gx对话.txt')
        
