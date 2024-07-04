import requests as rq

res = rq.get('https://automatetheboringstuff.com/files/rj.txt')

print(type(res))
print(res.status_code == rq.codes.ok)

print(len(res.text))

print(res.text[:250])

try:
    res.raise_for_status()
except Exception as exc:
    print("There was a problem: %s" %(exc))