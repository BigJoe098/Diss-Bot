import os
import shutil

def create_sticker(Group,Original,Name):
    
    #initilise the variables
    CurrentDir = os.getcwd()+"\\Assets\\"
    Name=Name+"."+Original.split(".")[-1]
    
    #code to check if group exists
    flag = True
    if not os.path.exists(CurrentDir+"StickerPacks\\"+Group):
        os.chdir(CurrentDir+"StickerPacks\\")
        os.mkdir(Group)
        os.chdir(CurrentDir)
        
    #Looking if a Sticker by that name already exists in the directory
    for x in os.listdir(CurrentDir+"StickerPacks\\"+Group+"\\"):
        if x.split(".")[0] == Name.split(".")[0]:
            os.remove(CurrentDir+"Temp\\"+Original)
            return "A Sticker With that Name Already Exists in this pack"
        
    #Sticker Processing
    source = CurrentDir+"Temp\\"+Original
    destination = CurrentDir+"\\StickerPacks\\"+Group+"\\"+Original
    
    #Moving to correct Location in sticker pack
    shutil.move(source,destination)
    
    #Renaming the sticker
    initial = CurrentDir+"\\StickerPacks\\"+Group+"\\"+Original
    result = CurrentDir+"\\StickerPacks\\"+Group+"\\"+Name
    os.rename(initial,result)
    
    return "Successfully Added New Sticker To Pack"

def delete_sticker(Group,Name):
    
    #initilise the variables
    CurrentDir = os.getcwd()+"\\Assets\\"

    #checking if the mentioned group exists
    if not os.path.exists(CurrentDir+"StickerPacks\\"+Group):
        return "Was unable to find a pack with that name."
    
    #Checking if the sticker exists
    flag = False
    for x in os.listdir(CurrentDir+"StickerPacks\\"+Group+"\\"):
        if x.split(".")[0] == Name:
            os.remove(CurrentDir+"StickerPacks\\"+Group+"\\"+x)
            flag = True

    #Deleting empty sticker pack
    if flag:
        if not os.listdir(CurrentDir+"StickerPacks\\"+Group+"\\"):
            shutil.rmtree(CurrentDir+"StickerPacks\\"+Group)

    #Outputing the response to user
    if flag:
        return "Successfully removed the sticker"
    else:
        return "Was not able to find a sticker with that name"
    
def getSticker(Group,Name):
    
    #initilise the variables
    CurrentDir = os.getcwd()+"\\Assets\\"

    #checking if the mentioned group exists
    if not os.path.exists(CurrentDir+"StickerPacks\\"+Group):
        return None,"Was unable to find a pack with that name."
    
    #Checking if the sticker exists
    for x in os.listdir(CurrentDir+"StickerPacks\\"+Group+"\\"):
        if x.split(".")[0] == Name:
            return x,(CurrentDir+"StickerPacks\\"+Group+"\\"+x)