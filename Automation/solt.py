##### importing libraries
try:
    import os
    import datetime
    import time
    import re
    import csv
    import pandas as pd
    from  pywinauto.application import Application
    from pywinauto import mouse
    from pywinauto import keyboard as kb
    from PIL import Image, ImageGrab
    import pytesseract as pt
    pt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
except:
    print("there is some error in importing libraries !!! please download the required libraries or more then one file open")
    exit()
####### csv list
try:
    a=[]
    csv_path = r'C:\Users\shuno\Desktop\sol_input.csv'
    with open(csv_path) as f:
        reader = csv.reader(f)
        for row in reader:
            a.append(row)
    print(a,len(a),sep='\n')
except:
    print("there is some error in opening csv file, check the specified path")
    exit()

##### starting application and maxmimizing it 
try:
    print('1')
    app = Application(backend='uia').start(r"C:\\SolTrace\\3.1.0\\x64\\soltrace.exe").connect(title='SolTrace 3.1.0 (64 bit): untitled')
    print('2')
    menub = app.SolTraceBitUntitled.child_window(title="Maximize", control_type="Button").wrapper_object()
    print('3')
    menub.click_input()
    print('4')
except:
    print("There is some error in opening app, check path and title of window")
    exit()

###### defining class sun
try:
    class Sun:
        def gotosun():
            mouse.click(coords=(60,70))
        def set_x(x):
            mouse.click(coords=(250,200))
            kb.send_keys("^a")
            kb.send_keys(x)
        def set_y(y):
            mouse.click(coords=(400,200))
            kb.send_keys("^a")
            kb.send_keys(y)
        def set_z(z):
            mouse.click(coords=(550,200))
            kb.send_keys("^a")
            kb.send_keys(z)
except:
    print("There is some error in defining class sun")
    exit()

##### defining class gotoptics:
try:
    class gotoptics:
        def clickoptics():
            mouse.click(coords=(150,70))
except:
    print("there is some error in clicking on optics check the parameter you sent")    
    exit()
    
##### defining class add optical properties1:
try:
    class addopticalproperties1:
        def clickaddopticalproperties1(nam,ref,tran,slop,spec,real):
            mouse.click(coords=(10,100))
            mouse.click(coords=(200,150))
            kb.send_keys("^a")
            kb.send_keys(nam)
            mouse.click(coords=(250,220))
            kb.send_keys("^a")
            kb.send_keys(ref)
            mouse.click(coords=(250,260))
            kb.send_keys("^a")
            kb.send_keys(tran)
            mouse.click(coords=(250,290))
            kb.send_keys("^a")
            kb.send_keys(slop)
            mouse.click(coords=(250,310))
            kb.send_keys("^a")
            kb.send_keys(spec)
            mouse.click(coords=(600,360))
            kb.send_keys("^a")
            kb.send_keys(real)            
except:
    print("there is some error in clicking on add optical check the parameter you sent")    
    exit()
##### defining class add optical properties2:
try:
    class addopticalproperties2:
        def clickaddopticalproperties2(nam,ref,tran,slop,spec,real):
            mouse.click(coords=(10,100))
            mouse.click(coords=(200,150))
            kb.send_keys("^a")
            kb.send_keys(nam)
            mouse.click(coords=(250,220))
            kb.send_keys("^a")
            kb.send_keys(ref)
            mouse.click(coords=(250,260))
            kb.send_keys("^a")
            kb.send_keys(tran)
            mouse.click(coords=(250,290))
            kb.send_keys("^a")
            kb.send_keys(slop)
            mouse.click(coords=(250,310))
            kb.send_keys("^a")
            kb.send_keys(spec)
            mouse.click(coords=(600,360))
            kb.send_keys("^a")
            kb.send_keys(real)            
except:
    print("there is some error in clicking on add optical check the parameter you sent")    
    exit()
    
##### defining class gotogeometry:
try:
    class gotogeometry:
        def clickgeometry():
            mouse.click(coords=(240,70))
except:
    print("there is some error in clicking on optics check the parameter you sent")    
    exit()

#### defining add stage
try:
    class addstage1:
        def addstage(nam):
            mouse.click(coords=(10,100))
            kb.send_keys("^a")
            kb.send_keys(nam)
            mouse.click(coords=(820,190))
            kb.send_keys("4")
            mouse.click(coords=(980,570))
        def chkpnt():
            mouse.click(coords=(90,370))
        def edit(x,y,z,Apper,surf,reftype,opti,comment):
            mouse.click(coords=(130,370))
            mouse.click(coords=(130,370))
            kb.send_keys(x)
            mouse.click(coords=(210,370))
            mouse.click(coords=(210,370))
            kb.send_keys(y)
            mouse.click(coords=(300,370))
            mouse.click(coords=(300,370))
            kb.send_keys(z)
            mouse.click(coords=(800,370))
            mouse.click(coords=(800,370))
            kb.send_keys(Apper)
            mouse.click(coords=(950,370))
            mouse.click(coords=(950,370))
            kb.send_keys(surf)
            mouse.click(coords=(1150,370))
            mouse.click(coords=(1150,370))
            mouse.click(coords=(1150,370))
            if(reftype=="refraction"):
                mouse.click(coords=(1150,390))
            if(reftype=="reflection"):
                mouse.click(coords=(1150,400))
            mouse.click(coords=(1300,370))
            mouse.click(coords=(1300,370))
            kb.send_keys(opti)
            mouse.click(coords=(1450,370))
            mouse.click(coords=(1450,370))
            kb.send_keys(comment)
except:
    print("there is some error in defining stage part1")
##### adding stage 2
try:
    class addstage2:
        def gosee2():
            mouse.click(coords=(20,135))
        def chkpnt():
            mouse.click(coords=(90,390))
            mouse.click(coords=(90,390))
                
        def edit(x,y,z,Apper,surf,reftype,opti,comment):
            mouse.click(coords=(130,390))
            mouse.click(coords=(130,390))
            kb.send_keys(x)
            mouse.click(coords=(210,390))
            mouse.click(coords=(210,390))
            kb.send_keys(y)
            mouse.click(coords=(300,390))
            mouse.click(coords=(300,390))
            kb.send_keys(z)
            mouse.click(coords=(800,390))
            mouse.click(coords=(800,390))
            kb.send_keys(Apper)
            mouse.click(coords=(950,390))
            mouse.click(coords=(950,390))
            kb.send_keys(surf)
            mouse.click(coords=(1150,390))
            mouse.click(coords=(1150,390))
            mouse.click(coords=(1150,390))
            if(reftype=="refraction"):
                mouse.click(coords=(1150,410))
            if(reftype=="reflection"):
                mouse.click(coords=(1150,420))
            mouse.click(coords=(1300,390))
            mouse.click(coords=(1300,390))
            kb.send_keys(opti)
            mouse.click(coords=(1450,390))
            mouse.click(coords=(1450,390))
            kb.send_keys(comment)
except:
    print("there is some error in defining stage part2")
#### add stage 3
try:
    class addstage3:
        def chkpnt():
            mouse.click(coords=(90,410))
            mouse.click(coords=(90,410))
                
        def edit(x,y,z,Apper,surf,reftype,opti,comment):
            mouse.click(coords=(130,410))
            mouse.click(coords=(130,410))
            kb.send_keys(x)
            mouse.click(coords=(210,410))
            mouse.click(coords=(210,410))
            kb.send_keys(y)
            mouse.click(coords=(300,410))
            mouse.click(coords=(300,410))
            kb.send_keys(z)
            mouse.click(coords=(800,410))
            mouse.click(coords=(800,410))
            kb.send_keys(Apper)
            mouse.click(coords=(950,410))
            mouse.click(coords=(950,410))
            kb.send_keys(surf)
            mouse.click(coords=(1150,410))
            mouse.click(coords=(1150,410))
            mouse.click(coords=(1150,410))
            if(reftype=="refraction"):
                mouse.click(coords=(1150,430))
            if(reftype=="reflection"):
                mouse.click(coords=(1150,440))
            mouse.click(coords=(1300,410))
            mouse.click(coords=(1300,410))
            kb.send_keys(opti)
            mouse.click(coords=(1450,410))
            mouse.click(coords=(1450,410))
            kb.send_keys(comment)
except:
    print("there is some error in defining stage part3")
#### add stage 4
try:
    class addstage4:
        def chkpnt():
            mouse.click(coords=(90,430))
            mouse.click(coords=(90,430))
                
        def edit(x,y,z,Apper,surf,reftype,opti,comment):
            mouse.click(coords=(130,430))
            mouse.click(coords=(130,430))
            kb.send_keys(x)
            mouse.click(coords=(210,430))
            mouse.click(coords=(210,430))
            kb.send_keys(y)
            mouse.click(coords=(300,430))
            mouse.click(coords=(300,430))
            kb.send_keys(z)
            mouse.click(coords=(800,430))
            mouse.click(coords=(800,430))
            kb.send_keys(Apper)
            mouse.click(coords=(950,430))
            mouse.click(coords=(950,430))
            kb.send_keys(surf)
            mouse.click(coords=(1150,430))
            mouse.click(coords=(1150,430))
            mouse.click(coords=(1150,430))
            if(reftype=="refraction"):
                mouse.click(coords=(1150,450))
            if(reftype=="reflection"):
                mouse.click(coords=(1150,460))
            mouse.click(coords=(1300,430))
            mouse.click(coords=(1300,430))
            kb.send_keys(opti)
            mouse.click(coords=(1450,430))
            mouse.click(coords=(1450,430))
            kb.send_keys(comment)
except:
    print("there is some error in defining stage part4")

###### adding new stage 5
try:
    class addstage5:
        def gosee5():
            mouse.click(coords=(120,135))
        def addstage(nam):
            mouse.click(coords=(10,100))
            kb.send_keys("^a")
            kb.send_keys(nam)
            mouse.click(coords=(820,190))
            kb.send_keys("1")
            mouse.click(coords=(980,570))
        def chkpnt():
            mouse.click(coords=(90,370))
        def edit(x,y,z,Apper,surf,reftype,opti,comment):
            mouse.click(coords=(130,370))
            mouse.click(coords=(130,370))
            kb.send_keys(x)
            mouse.click(coords=(210,370))
            mouse.click(coords=(210,370))
            kb.send_keys(y)
            mouse.click(coords=(300,370))
            mouse.click(coords=(300,370))
            kb.send_keys(z)
            mouse.click(coords=(800,370))
            mouse.click(coords=(800,370))
            kb.send_keys(Apper)
            mouse.click(coords=(950,370))
            mouse.click(coords=(950,370))
            kb.send_keys(surf)
            mouse.click(coords=(1150,370))
            mouse.click(coords=(1150,370))
            mouse.click(coords=(1150,370))
            if(reftype=="refraction"):
                mouse.click(coords=(1150,390))
            if(reftype=="reflection"):
                mouse.click(coords=(1150,400))
            mouse.click(coords=(1300,370))
            mouse.click(coords=(1300,370))
            kb.send_keys(opti)
            mouse.click(coords=(1450,370))
            mouse.click(coords=(1450,370))
            kb.send_keys(comment)
except:
    print("there is some error in defining stage part5")
##### defining class gotoraytrace:
try:
    class gotoraytrace:
        def clickraytrace():
            mouse.click(coords=(380,70))
        def startraytrace():
            mouse.click(coords=(600,165))
except:
    print("there is some error in opening soltrace objebt,check coordinate")

##### defining class viewres:
try:
    class fluxres:
        def clickfmaps():
            mouse.click(coords=(680,70))
        def clickviewmap():
            mouse.click(coords=(15,120))
        def fluxread():
            flag=0
            heatimg = ImageGrab.grab(bbox = (455, 82, 1920, 790))
            heatimg.save(r'C:\Users\shuno\Desktop\test_img\{}_flux.png'.format(i))
            fimg = ImageGrab.grab(bbox = (450, 785, 1020, 1020))
            #fimg.show()
            tesstr = pt.image_to_string(fimg,lang ='eng')
            print(tesstr)
            strlist = tesstr.split('\n')
            flux_res=None
            for x in strlist:
                if re.search('Avg. flux:',x):
                    f_str=(x.split(':')[-1]).strip()
                    f_str = f_str.replace('$','9')
                    if '+' in f_str:
                        num_str=(f_str.split('+')[0])[:-1]
                        print(num_str)
                        num_str_split=re.split('\D',num_str)
                        num_str=num_str_split[0]+'.'+num_str_split[-1]
                        exp_str=(f_str.split('+')[-1])
                        flux_res=float(num_str)*(10**float(exp_str))
                    else:
                        flux_res=float(f_str)
                    fimg.save(r'C:\Users\shuno\Desktop\test_img\{}_dat.png'.format(i))
                    flag+=1
            if flag==0:
                fimg.save(r'C:\Users\shuno\Desktop\test_img\{}_None.png'.format(i))
            # print(flux_res,type(flux_res))
            return flux_res
except:
    print("there is some error in image processing")

gotoptics.clickoptics()
addopticalproperties1.clickaddopticalproperties1("concentrator","1","1","3","0.5","1.1")
addopticalproperties2.clickaddopticalproperties2("absorber","0","0","0.0001","0.0001","1")

gotogeometry.clickgeometry()
addstage1.addstage("reflector")
addstage1.edit("0","0","0",f"c-{a[0][4]},0,0,0,0,0,0,0",f"p-{a[0][6]},{a[0][7]},0,0,0,0,0,0","Reflection","concentrator","parabolic")
addstage2.edit("0","0","0",f"c-{a[0][4]},0,0,0,0,0,0,0",f"p-{a[0][6]},{a[0][7]},0,0,0,0,0,0","Reflection","concentrator","paraboloid")
addstage3.edit("0","0","0",f"c-{a[0][4]},0,0,0,0,0,0,0",f"p-{a[0][6]},{a[0][7]},0,0,0,0,0,0","Reflection","concentrator","spherical")
addstage4.edit("0","0","0",f"c-{a[0][4]},0,0,0,0,0,0,0",f"p-{a[0][6]},{a[0][7]},0,0,0,0,0,0","Reflection","concentrator","elliptical_parboloid")
addstage1.chkpnt()
addstage1.chkpnt()
addstage2.chkpnt()
addstage3.chkpnt()
addstage4.chkpnt()
addstage5.addstage("collector")
addstage5.edit("0","0",f"{a[0][8]}","c-0.03,0,0,0,0,0,0,0","f-0,0,0,0,0,0,0,0","Reflection","absorber","flat_round")

save_path = r'C:\Users\shuno\Desktop\sol_input_pls.csv'
flux_lst=[]
for i in range(49,len(a)):
    #range(1,len(a)+1)
    Sun.gotosun()
    Sun.set_x(a[i][0])
    Sun.set_y(a[i][1])
    Sun.set_z(a[i][2])
    gotogeometry.clickgeometry()
    mark = False
    addstage2.gosee2()
    if(a[i][5]=='p'):
        addstage2.edit("0","0","0",f"{a[i][3]}-{a[i][4]},0,0,0,0,0,0,0",f"{a[i][5]}-{a[i][6]},{a[i][7]},0,0,0,0,0,0","Reflection","concentrator","paraboloid")
        addstage2.chkpnt()
        mark = True
    if(a[i][5]=='s'):
        addstage3.edit("0","0","0",f"{a[i][3]}-{a[i][4]},0,0,0,0,0,0,0",f"{a[i][5]}-{a[i][6]},{a[i][7]},0,0,0,0,0,0","Reflection","concentrator","spherical")       
        addstage3.chkpnt()
    addstage5.gosee5()
    addstage5.edit("0","0",f"{a[i][8]}",f"{a[i][9]}-{a[i][10]},0,0,0,0,0,0,0",f"{a[i][11]}-{a[i][12]},{a[i][13]},0,0,0,0,0,0","Reflection","absorber","flat_round")
    gotoraytrace.clickraytrace()
    gotoraytrace.startraytrace()
    fluxres.clickfmaps()
    fluxres.clickviewmap()
    flux_str = fluxres.fluxread()
    gotogeometry.clickgeometry()
    addstage2.gosee2()
    if(a[i][5]=='p'):
        addstage2.chkpnt()
        mouse.click(coords=(90,390))
    else:
        addstage3.chkpnt()
        mouse.click(coords=(90,410))
    flux_lst.append(flux_str)
    print("Avg. flux is: {}".format(flux_str))
    try:
        print('10')
        df = pd.read_csv(save_path)
        print('20')
        df.loc[i-1, 'Avg_Flux'] = flux_str
        print('30')
        df.to_csv(save_path, index=False)
        print('40')
    except:
        print("there is some error in opening csv file, check the specified path")
        exit()
    print("Avg. flux is: {}".format(flux_str))

print(flux_lst)

save_path2 = r'C:\Users\shuno\Desktop\sol_input_bkup.csv'
try:
    print('100')
    for i in range(len(flux_lst)):
        print('200-',i)
        df = pd.read_csv(csv_path)
        print('300-',i)
        df.loc[i, 'Avg_Flux'] = flux_lst[i]
        print('400-',i)
    print(df)
    print('500')
    df.to_csv(save_path2, index=False)
    print('600')
except:
    print("there is some error in opening csv file, check the specified path 0000")
    exit()
# Sun.set_x("0")
# Sun.set_y("10")
# Sun.set_z("100")
# gotoptics.clickoptics()
# addopticalproperties1.clickaddopticalproperties1("concentrator","1","1","3","0.5","1.1")
# addopticalproperties2.clickaddopticalproperties2("absorber","0","0","0.0001","0.0001","1")
# gotogeometry.clickgeometry()
# addstage1.addstage("reflector")
# addstage1.chkpnt()
# addstage2.chkpnt()
# # addstage3.chkpnt()
# addstage4.chkpnt()
# addstage5.addstage("collector")
# # addstage5.chkpnt()
# gotoraytrace.clickraytrace()
# gotoraytrace.startraytrace()

# fluxres.clickfmaps()
# fluxres.clickviewmap()
# flux_str = fluxres.fluxread()
# print("Avg. flux is: {}".format(flux_str))