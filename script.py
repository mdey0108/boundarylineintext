import os
import json
from cv2 import cv2



def func(direc):
    

    for file in os.listdir(direc):
        if file.endswith(".json"):


        #     print(os.path.join(direc,file))
        # else:
        #     print(os.path.join(direc,file),"it is a JPG file")
            try:
                myjsonfile = open(os.path.join(direc, file), "r")
                jsondata=myjsonfile.read()

                # parsing of data----------------
                obj=json.loads(jsondata)
                # print(obj['version'])
                sp=obj['shapes']
                imm=obj["imagePath"]

                i_m=imm.split("\\")
                iim=i_m[-1]
                # im="C:\\Users\\INDIAN\\Desktop\\gahan AI\\Data_Set\\Data_Set\\"+iim
                im=direc+"\\"+iim
                # img=r"20201028_163259.jpg"
                # print(im)
                img=cv2.imread(im)
                # print(img)
                # print(sp)
                ab=list(obj['shapes'])
                # print(ab)

                for i in range(len(ab)):
                    ac=dict(ab[i])
                    # print(ac["points"])
                    ad=list(ac["points"])
                    # print(ad)
                    w, x, y, z=ad[0], ad[1], ad[2], ad[3]
                    x1, y1=int(w[0]), int(w[1])
                    x2, y2=int(x[0]), int(x[1])
                    x3, y3=int(y[0]), int(y[1])
                    x4, y4=int(z[0]), int(z[1])


                    # print (x)
                    # cv2.rectangle(img,(x1,y1),(x3,y3),(255, 0, 0),2)

                    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), thickness=1)
                    cv2.line(img, (x2, y2), (x3, y3), (0, 255, 0), thickness=1)
                    cv2.line(img, (x3, y3), (x4, y4), (0, 255, 0), thickness=1)
                    cv2.line(img, (x4, y4), (x1, y1), (0, 255, 0), thickness=1)
                ed="json applied "+iim
                cv2.imshow(ed, img)
                path = 'Data_Set/Images'
                cv2.imwrite(os.path.join(path , ed), img)
                cv2.waitKey(1)

            except:
                print("something went wrong with ", file , "\nimagepath is incorrect")


direc = "Data_Set\\Data_Set"
func(direc)


