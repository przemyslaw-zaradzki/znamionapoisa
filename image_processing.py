from Model import transforms_array, get_prediction

def processing(path):
    class_names = [ 'choroba Bowena',
    'rak podstawnokomórkowy',
    'łagodne rogowacenie',
    'dermatofibroma',
    'czerniak',
    'znamię melanocytowe',
    'zmiana naczyniowa' ]
    #img, gray_blur = read_img("static\images\skinn.jpg")
    #tensor = transforms_array(img)
    tensor = transforms_array("static/images/skinn.jpg")
    prediction = get_prediction(tensor)
    print(class_names[int(prediction)])
    return class_names[int(prediction)]