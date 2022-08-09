import json


def request_blockData(block, block_type):
    with open("code_blocks.json", 'r') as file:
        i = json.load(file)
        print(i)
        e = i['block_dat']
        print(e)
        if block in e:
            print("In Data")
            t = e[block]
            if str(block_type) in t:
                print("EEEEEEEEEE")
                return t[str(block_type)]





test = request_blockData("conditional_blocks", "If Statement")

#Test
print(test)