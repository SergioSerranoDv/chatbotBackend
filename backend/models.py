from .utils import db   

# Create your models here.
class Website_Model: 
   def __init__(self):
      self.collection = db['website']
      
   def get_all_websites(self):
      return list(self.collection.find({}))
     