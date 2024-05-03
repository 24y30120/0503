import base64 as b64

학번 = []

학번.append(int(b64.b64decode("Mw==").decode().format("utf-8")))
학번.append(int(b64.b64decode("MA==").decode().format("utf-8")))
학번.append(int(b64.b64decode("MQ==").decode().format("utf-8")))
학번.append(int(b64.b64decode("Mg==").decode().format("utf-8")))
학번.append(int(b64.b64decode("MA==").decode().format("utf-8")))

for i in 학번:
    print(i, end="")

print()

이름 = ["허", "준"]
for i in 이름:
    print(i, end="")