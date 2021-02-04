import json
a=[[1,2],[3,4],[5,6]]
b=json.loads(json.dumps(a))
a[0][0]=100000
a[2][1]=69
print(b)
