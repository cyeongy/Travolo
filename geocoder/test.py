import pickle


data = [1, 3, 2]
end = 0
res = []

try:
    with open('./not_found_list.bin', 'rb') as f:
        not_found_list = pickle.load(f)
        t = set(not_found_list)
        not_found_list = list(t)
        not_found_list.sort()
        not_found_list_idx = len(not_found_list)
        point = pickle.load(f)
except Exception as e:
    print(e)


# with open('./not_found_list.bin', 'wb') as f:
#     pickle.dump(not_found_list, f)
#     pickle.dump(point, f)

print(not_found_list)
print(not_found_list_idx, point)



try:
    with open('./sample_data.bin', 'rb') as f:
        res = pickle.load(f)
        end = pickle.load(f)
        print(data, end)
except Exception:
    pass

print(data)
t = set(data)
print(data)
data = list(t)


with open('./sample_data.bin', 'wb') as f:
    end = end+1
    pickle.dump(data, f)
    pickle.dump(end, f)
    print(data, end)


