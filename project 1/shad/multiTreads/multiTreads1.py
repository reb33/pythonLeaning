from threading import Thread


def test(part_index, inputs, outputs):
    output = inputs[part_index] ** 2
    outputs[part_index] = output

SIZE = 5
inputs = range(SIZE)
outputs = [None for i in inputs]

threads = []
for i in range(SIZE):
    t = Thread(target= test, args= (i, inputs, outputs))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print(outputs)

