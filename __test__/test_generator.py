
def sqaures(n=10):
    for i in range(n):
        # return은 한 번 리턴하고 끝이나, yield는 루프안에서 매 번 반환하고 다시 돌아와서 수행한다.(루프 끝날때까지)
        yield(i, i**2)


for x in sqaures(20):
    print(x)