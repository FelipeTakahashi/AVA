firstV = [float(a) for a in input().split()]

secondV = [float(a) for a in input().split()]

answerV = []
for i in range(3):
    answer_item = firstV[i] + secondV[i]
    answerV.append(answer_item)
    print(f"{answerV[i]:.2f} ", end='')
