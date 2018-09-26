#This function will download and resize all images in the imageLinks folder and will split into train and test folders with their associated label.

#Editor's note: It is your responsibility to ensure that use of copyrighted images accessed in connection with this script complies with any license restrictions that may apply.

copyLabels = True
trainPercent = 0.85

listing = os.listdir(linksPath) 
for classes in listing:
    os.chdir(linksPath)
    text = open(classes, 'r')
    links = text.readlines()
    links = [i.strip() for i in links]
    
    cut = int(np.floor(len(links)*trainPercent))
    
    for i in range(cut):
        os.chdir(trainPath)
        if check(links[i]):
            image = skimage.io.imread(links[i])
            image = skimage.transform.resize(image, [300,300])
            skimage.io.imsave(classes[:-4]+str(i)+'.jpg', image)
            if copyLabels:
                label = classes[:-4]+str(i)+'.xml'
                shutil.copyfile(labelsPath+'/'+label,trainPath+'/'+label) 
        
    for i in range(cut,len(links)):
        os.chdir(testPath)
        if check(links[i]):
            image = skimage.io.imread(links[i])
            image = skimage.transform.resize(image, [300,300])
            skimage.io.imsave(classes[:-4]+str(i)+'.jpg', image)
            if copyLabels:
                label = classes[:-4]+str(i)+'.xml'
                shutil.copyfile(labelsPath+'/'+label,testPath+'/'+label) 
