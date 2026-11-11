dirty_data = ["88", "hello", "90", "world", "75"]
print(f"{dirty_data}")
dirty_data[0]="99"
print(f"{dirty_data}")
dirty_data.append("lll")
print(f"{dirty_data}")
index=dirty_data.index("hello")
print(index)
dirty_data.remove("90")
print(f"{dirty_data}")
print(dirty_data[:-1])
dirty_data.insert(2,"909090")
print(f"{dirty_data}")
print(dirty_data[::-1])