import re 
def activity (x):
    x = x.lower()
    
    diving = re.findall (r'diving | \.*\diving\.*', str(x))
    swimming = re.findall (r'swimming |\.*swim\.*', str(x))
    sailing = re.findall (r'sailing | \.*\sail\.*', str(x))
    paddling = re.findall (r'paddling | \.*paddling\.*', str(x))
    fishing = re.findall (r'fishing | \.*fishing\.*', str(x))
    surfing = re.findall (r'surfing |.*surf.*', str(x))
    snorkeling = re.findall (r'snorkeling | \.*\snorkeling\.* | \.*\snorkel\.*', str(x))
    kayaking = re.findall (r'kayaking | \.*kayaking\.* | \.*kayak\.*', str(x))
    
    
    if diving:
        return 'Diving'
    if swimming:
        return 'Swimming'
    if sailing:
        return 'Sailing'
    if paddling:
        return 'Paddling'
    if fishing:
        return 'Fishing'
    if surfing:
        return 'Surfing'
    if snorkeling:
        return 'Snorkeling'
    if kayaking:
        return 'Kayaking'
    else:
        return 'Unknown activity'

def species (y):
    y=str(y)
    y = y.lower()
    
    white = re.findall(r'white | \.*\white\.*', str(y))
    tiger = re.findall (r'tiger | \.*\tiger\.*', str(y))
    bull = re.findall (r'bull | \.*\bull\.*', str(y))
    lemon = re.findall (r'lemon | \.*lemon\.*', str(y))
    reef = re.findall (r'reef | \.*reef\.*', str(y))

    if white:
        return 'White shark'
    if tiger:
        return 'Tiger shark'
    if bull:
        return 'Bull shark'
    if lemon:
        return 'Lemon shark'
    if reef:
        return 'Reef shark'
    else:
        return 'Species unknown'






        


