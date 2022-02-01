import ujson

if __name__ == '__main__':
    json_str = '{"age": 2, "height": 3.4}'
    obj = ujson.loads(json_str)
    print(obj)