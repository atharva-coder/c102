from pickle import FALSE
import cv2
import dropbox
import time
import random

start_time=time.time()
def take_snapshot():
    number=random.randint(0,100)
    vco=cv2.VideoCapture(0)
    results=True
    while(results):
        ret,frame=vco.read()
        img_name='img'+str(number)+'.png'
        cv2.imwrite(img_name,frame)
        start_time=time.time
        results=False
    return img_name
    print("snapshot taken")
    vco.release()
    cv2.destroyAllWindows()
def upload_file(img_name):
    access_token='sl.BH5KezbYL5IAnqi0BRXoawpPnokyoKLg5yCQmsXCy0P50gxN0uE426DLBgE4dlvszFdo9qpceV4xmuJ-K16BV1h_1Nc3Kvx6l_FHrTGBa9l2vVQZJZ3ab3LNAE_wUjiuQejkNG6Ftk8'
    file=img_name
    file_from=file
    file_to="/c102/"+img_name
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")
def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapshot()
            upload_file(name)
main()            



