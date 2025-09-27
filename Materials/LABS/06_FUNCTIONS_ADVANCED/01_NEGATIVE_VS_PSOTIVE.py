def pos_vs_neg(seq):
    neg = 0
    pos =0
    result = ''

    for num in seq:
        if num < 0:
           neg + (abs(num))
        elif num > 0:
            pos += num

    if abs(sum(neg)) > sum(pos):
        result = 'The negatives are stronger than the positives'
    elif abs(sum(pos)) > sum(neg):
        result = 'The positives are stronger than the negatives'

    return f'{sum(neg)}\n{ sum(pos)}\n{result}'

sequence = list(map(int,input().split()))

print(pos_vs_neg(sequence))