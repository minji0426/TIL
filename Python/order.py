def solution(order_times, k):
    answer = 0

    for i in range(len(order_times)):
        HH, MM = map(int, order_times[i].split(':'))
        minute = 60 * HH + MM + k

        for j in range(i + 1, len(order_times)):
            HH2, MM2 = map(int, order_times[j].split(':'))
            minute2 = 60 * HH2 + MM2
            # print(minute, minute2)

            if minute2 > minute:
                answer = max(answer, j - i)
                # print(j - i)
                break


    return answer


order_times = ["12:10", "12:20", "12:40", "12:40", "12:50", "13:00", "13:20"]
k = int(input())
print(solution(order_times, k))
