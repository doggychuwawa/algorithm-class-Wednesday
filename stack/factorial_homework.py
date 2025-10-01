#############################################################################
#  시스템 스택 호출과 재귀함수를 이용한 팩토리얼 계산 콘솔 인터렉티브 프로그램 
#  작성자: 김현서
#  작성일: 2025-09-28
#############################################################################

import time

# 반복문 기반 팩토리얼
def factorial_iter(n: int) -> int:
    if n < 0:
        raise ValueError("오튜")
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result

# 재귀 기반 팩토리얼
def factorial_rec(n: int) -> int:
    if n < 0:
        raise ValueError("오류")
    
    if n in (0, 1):
        return 1
    
    return n * factorial_rec(n - 1)

# 실행 시간 측정 함수
def run_with_time(func, n: int):
    start = time.time()
    result = func(n)
    elapsed = time.time() - start
    return result, elapsed

# 테스트 데이터
TEST_DATA = [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]

# 메인 인터랙티브 함수
def main():
    while True:
        print("\n*** 팩토리얼 계산기 ***")
        print("1. 반복문으로 팩토리얼 계산")
        print("2. 재귀로 팩토리얼 계산")
        print("3. 두 방식 비교")
        print("4. 테스트 데이터 일괄 실행")
        print("q. 종료")

        choice = input("메뉴 선택: ").strip()

        if choice in ["1", "2", "3"]:
            n_str = input("n 값을 입력하세요: ").strip()
            if not n_str.isdigit():
                print("⚠️ 오류: 정수를 입력하세요.")
                continue
            n = int(n_str)

            try:
                if choice == "1":
                    result, elapsed = run_with_time(factorial_iter, n)
                    print(f"[반복] {n}! = {result}")
                    print(f"실행 시간: {elapsed:.6f}초")

                elif choice == "2":
                    result, elapsed = run_with_time(factorial_rec, n)
                    print(f"[재귀] {n}! = {result}")
                    print(f"실행 시간: {elapsed:.6f}초")
                    
                elif choice == "3":
                    iter_res, iter_time = run_with_time(factorial_iter, n)
                    rec_res, rec_time = run_with_time(factorial_rec, n)
                    print(f"\n▶ {n}! 결과 비교")
                    print(f"결과 일치 여부: {iter_res == rec_res}\n")
                    
                    print(f"[반복문]")
                    print(f"결과: {iter_res}")
                    print(f"실행 시간: {iter_time:.6f}초\n")
                    
                    print(f"[재귀함수]")
                    print(f"결과: {rec_res}")
                    print(f"실행 시간: {rec_time:.6f}초")

            except ValueError as e:
                print(f"오류: {e}")
            
        elif choice == "4":
            for n in TEST_DATA:
                print(f"\n--- n = {n} ---")
                try:
                    iter_res, iter_time = run_with_time(factorial_iter, n)
                    rec_res, rec_time = run_with_time(factorial_rec, n)
                    print(f"{n}! 결과 일치 여부: {iter_res == rec_res}")
                    print(f"[반복] 실행 시간: {iter_time:.6f}초")
                    print(f"[재귀] 실행 시간: {rec_time:.6f}초")
                    print(f"결과값: {iter_res}")
                except RecursionError:
                    print(f"{n}! 재귀 계산 중 RecursionError 발생")

        elif choice == "q":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택하세요.")

if __name__ == "__main__":
    main()