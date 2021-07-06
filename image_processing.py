from Model import transforms_array, get_prediction

def processing():
    class_names = [ 'choroba Bowena',
    'rak podstawnokomórkowy',
    'łagodne rogowacenie',
    'dermatofibroma',
    'czerniak',
    'znamię melanocytowe',
    'zmiana naczyniowa' ]
    tensor = transforms_array("static/images/skinn.jpg")
    prediction, probabilities = get_prediction(tensor)
    print(class_names[int(prediction)])
    return class_names, prediction, probabilities
