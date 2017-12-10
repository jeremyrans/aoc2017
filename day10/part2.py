input = [ord(i) for i in "197,97,204,108,1,29,5,71,0,50,2,255,248,78,254,63"]
input += [17, 31, 73, 47, 23]

numbers = range(0, 256)
size = len(numbers)
cur_pos = 0
skip_size = 0

for _ in xrange(64):
    for i in input:
        if (cur_pos + i) > size:
            end = numbers[cur_pos:]
            start = numbers[:i-len(end)]
            sub_list = list(reversed(end + start))
            numbers = sub_list[-len(start):] + numbers[len(start):cur_pos] + sub_list[:len(end)]
        else:
            sub_list = list(reversed(numbers[cur_pos:cur_pos + i]))
            numbers = numbers[:cur_pos] + sub_list + numbers[cur_pos + i:]
        cur_pos += (i + skip_size)
        cur_pos = cur_pos % size
        skip_size += 1


hash = ''
for x in xrange(0, 256, 16):
    output = 0
    for i in numbers[x:x+16]:
        output = output ^ i

    hash += hex(output)[2:]

print hash
