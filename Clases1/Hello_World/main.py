import requests

def main():
 #   url= 'https://httpbin.org/get'
  #  params={
   #     'key':'value1',
    #}
    #payload={
     #   'key':'value2',
    #}
    #headers={
     #   'Content-Type':'application/json'
      #  'Authorization:Bearer YOUR_ACCESS_TOKEN'
    #}

    # response=requests.get(url,params=params,data=payload,headers=headers)

    def suma(data):
        a= data.get('a')
        b= data.get('b')
        return a+b
    
    data={"a":"5|","b":"10"}
 
    resultado=suma(data)    
    print(resultado)