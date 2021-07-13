from Model import transforms_array, get_prediction

def processing(img_name):
    class_names = [ 'choroba Bowena',
    'rak podstawnokomórkowy',
    'łagodne rogowacenie',
    'dermatofibroma',
    'czerniak',
    'znamię melanocytowe',
    'zmiana naczyniowa' ]
    tensor = transforms_array("static/images/"+img_name)
    prediction, probabilities = get_prediction(tensor)
    return class_names, prediction, probabilities