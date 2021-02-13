import json


buttonConfig = json.load(open("spiceShuttle.json"))

# for i in range(3):
#     print(buttonConfig["buttons"][i]["buttonLabel"])

for button in buttonConfig:
    print(button)