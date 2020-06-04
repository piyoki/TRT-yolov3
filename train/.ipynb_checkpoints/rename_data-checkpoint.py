# Pythono3 code to rename multiple  
# files in a directory or folder 

import os 
from PIL import Image
import time

DATA_DIR = 'train/data/'
  
# Function to rename multiple files 
def main(): 
    
    out = dict()
    items = list()
    imgs = list()
    xmls = list()
    
    t1 = time.time()
    
    for root, dirs, files in os.walk(DATA_DIR):
        for file in files:
            path = os.path.join(root, file)
            fileExt = os.path.splitext(file)[1].lower()
            if fileExt == '.xml':
                xmls.append(path)
            else:
                imgs.append(path)
    
    for img in imgs:
        _img = img.split('.')[0]
        for xml in xmls:
            _xml = xml.split('.')[0]
            if _img == _xml:
                item = (img,xml)
                items.append(item)
    
    for count, item in enumerate(items):
        out[count] = item
            
    for count in out:
        
        img = '.' + out[count][0].split('/')[-1].split('.')[-1]
        xml = '.' + out[count][1].split('/')[-1].split('.')[-1]
        
        if count > 9 and count < 99:
            dst_img = DATA_DIR + '000' + str(count) + img
            dst_xml = DATA_DIR + '000' + str(count) + xml
        elif count > 99 and count < 999:
            dst_img = DATA_DIR + '00' + str(count) + img
            dst_xml = DATA_DIR + '00' + str(count) + xml
        elif count > 999 and count < 9999:
            dst_img = DATA_DIR + '0' + str(count) + img
            dst_xml = DATA_DIR + '0' + str(count) + xml
        elif count > 9999:
            dst_img = DATA_DIR + str(count) + img
            dst_xml = DATA_DIR + str(count) + xml
        else:
            dst_img = DATA_DIR + '0000' + str(count) + img
            dst_xml = DATA_DIR + '0000' + str(count) + xml
        
        
        os.rename(out[count][1], dst_xml)
        os.rename(out[count][0], dst_img)
            
    t2 = time.time()
    
    print('Execute time:',str(round((t2-t1),4))+'s')
    print('Total %i imgs converted.'%len(out))
  

if __name__ == '__main__': 
    main()
