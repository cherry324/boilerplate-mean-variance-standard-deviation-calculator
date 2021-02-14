import numpy as np

def calculate(list):

  
  
  
  if len(list)!=9:
      raise ValueError('List must contain nine numbers.')
      
  else:
      a=np.reshape(list,(3,3))
  
      result={'mean': [np.mean(a, axis = 0).tolist(), np.mean(a, axis=1).tolist(), np.mean(a).tolist()], 
        'variance': [np.var(a, axis = 0).tolist(), np.var(a, axis=1).tolist(), np.var(a).tolist()], 
        'standard deviation': [np.std(a, axis = 0).tolist(), np.std(a, axis=1).tolist(), np.std(a).tolist()],
        'max': [np.amax(a, axis = 0).tolist(), np.amax(a, axis=1).tolist(), np.amax(a).tolist()],
        'min': [np.amin(a, axis = 0).tolist(), np.amin(a, axis=1).tolist(), np.amin(a).tolist()],
        'sum': [np.sum(a, axis = 0).tolist(), np.sum(a, axis=1).tolist(), np.sum(a).tolist()]}
      return result 
