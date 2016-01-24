import wolframalpha

class WolframController:
  
  def __init__(self):
    self.client = wolframalpha.Client("6JY563-7QT38QKE43")

  # Returns a list 
  def ask_question(self, question):
    res = self.client.query(question)

    # Query fails
    if len(res.pods) <= 0:
      return ["Sorry, we do not have an answer for that"]

    output = []
    for pod in res.pods:
        s = pod.text
        s = s.encode('ascii',errors='ignore')
        output += s.splitlines()
    
    

    # Query succeeds
    return output



