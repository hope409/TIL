# 모듈
## 개요
  - 과학자, 수학자가 모든 이론을 새로 만들거나 증명하지 않는 것처럼
  - 개발자 또한 프로그램 전체를 모두 혼자 힘으로 작성하는 것은 드문 일
  - 다른 프로그래머가 이미 작성해 놓은 수천, 수백만 줄의 코드를 활용하는 것은 생산성에서 매우 중요한 일
### 1. 모듈
---
  - 한 파일로 묶인 변수와 함수의 모음
  - 특정한 기능을 하는 코드가 작성된 파이썬 파일(.py)
#### 1) 모듈 예시
---
  - math 내장 모듈
    - 파이썬이 미리 작성해 둔 수학 관련 변수와 함수가 작성된 모듈
``` python
import math

print(math.pi) # 3.141592653589793

print(math.sqrt(4)) # 2.0
```
#### 2) 모듈 활용
 ---
#### 모듈을 가져오는 방법
---
  - import 문 사용
``` python
import math

print(math.sqrt(4))
```
  - from 절 사용
``` python
from math import sqrt
# 이렇게 쓰면 모듈의 함수? 내가 만든 함수? 무슨 모듈의 함수? 의문이 생긴다.
print(sqrt(4))
```
#### 3) 모듈 사용하기
---
  - '. (dot)' 연산자
    - "점의 왼쪽 객체에서 점의 오른쪽 이름을 찾아라" 라는 의미
``` python
import math
# 모듈명.변수명
print(math.pi)

print(math.sqrt(4))
```
#### 4) 모듈 주의사항
---
  - 서로 다른 모듈이 같은 이름의 함수를 제공할 경우 문제 발생
  - 마지막에 import된 이름으로 대체됨
``` python
from math import pi, sqrt
from my_math import sqrt
```

``` python
# 그래서 모듈 내 모든 요소를 한번에 import 하는 * 표기는 권장하지 않음

from math import * 
```
#### 5) 'as' 키워드
---
  - as 키워드를 사용하여 별칭(alias)을 부여
    - 두 개 이상의 모듈에서 동일한 이름의 변수, 함수 클래스 등을 가져올 때 발생하는 이름 충돌 해결
``` python
from math import sqrt
from my_math import sqrt as my_sqrt

sqrt(4)
my_sqrt(4)
```
### 2. 파이썬 표준 라이브러리
---
  - 파이썬 언어와 함께 제공되는 다양한 모듈과 패키지의 모음
### 3. 패키지
---
  - 연관된 모듈들을 하나의 디렉토리에 모아 놓은 것
#### 1) 패키지 사용하기
---
  - 아래와 같은 디렉토리 구조로 작성
  - 패키지 3개 : my_package, math, statistics
  - 모듈 2개 : my_math, tools
``` python
from my_package.math import my_math
from my_package.statistics import tools

print(my_math.add(3, 4)) # 7
print(tools.mod(1, 2)) # 1
```
### 4. PSL 내부 패키지
---
  - 설치 없이 바로 import하여 사용

### 5. 외부 패키지
---
  - pip를 사용하여 설치 후 import필요

#### 1) pip
---
  - 외부 패키지들을 설치하도록 도와주는 파이썬의 패키지 관리 시스템

#### 2) 패키지 설치
---
  - 최신 버전 / 특정 버전 / 최소 버전을 명시하여 설치할 수 있음
``` bash
pip install SomPackage
pip install SomPackage == 1.0.5
pip install SomPackage >= 1.0.4
```
##### requests 외부 패키지 설치 및 사용 예시
``` bash
pip install requests
```
``` python
import requests

url = '주소'
response = requests.get(url).json()

print(response)
```

#### 3) 패키지 사용 목적
---
  - 모듈들의 이름공간을 구분하여 충돌을 방지
  - 모듈들을 효율적으로 관리하고 재사용할 수 있도록 돕는 역할
### 6. 제어문
---
  - 코드의 실행 흐름을 제어하는 데 사용되는 구문
  - 조건에 따라 코드 블록을 실행하거나 반복적으로 코드를 실행
#### 1) 제어문
---
  - 조건문
    - if, elif, else
  - 반복문
    - for, while
  - 반복문 제어
    - break, continue, pass
#### 2) 조건문
---
  - 주어진 조건식을 평가하여 해당 조건이 참(True)인 경우에만 코드 블록을 실행하거나 건너뜀
> if statement의 기본구조
``` python
if 표현식:
  코드 블록
elif 표현식:
  코드 블록
else:
  코드 블록
```
##### 조건문 예시
``` python
a = 5
if a > 3:
  print('3 초과')
else:
  print('3 이하')

print(a) # 3 초과
```

``` python
a = 3
if a > 3:
  print('3 초과')
else:
  print('3 이하')

print(a) # 3 이하
```
#### 3) 복수 조건문
---
  - 조건식을 동시에 검사하는 것이 아니라 "순차적"으로 비교
``` python
dust = 35

if dust > 150:
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')
```

#### 4) 중첩 조건문
``` python
dust = 480

if dust > 150:
    print('매우 나쁨')
    if dust > 300:
        print('위험해요! 나가지 마세요!')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')
```

### 7. 반복문
---
- 주어진 코드 블록을 여러 번 반복해서 실행하는 구문
#### 1) for / while
---
- for : 특정 작업을 반복적으로 수행
- 주어진 조건이 참인 동안 반복해서 실행
파이썬 반복문에 사용되는 키워드

#### 2) for
---
  - 임의의 시퀀스의 항목들을 그 시퀀스에 들어있는 순서대로 반복
> for statement의 기본 구조
``` python
for 변수 in 반복 가능한 객체:
  코드 블록
```
#### 3) 반복 가능한 객체
---
  - 반복문에서 순회할 수 있는 객체
  - (시퀀스 객체 뿐만 아니라 dict, set 등도 포함)
#### 4) for문 작동원리
---
  - 리스트 내 첫 항목이 반복 변수에 할당되고 코드블록이 실행
  - 다음으로 반복 변수에 리스트의 2번째 항목이 할당되고 코드블록이 다시 실행
  - 마지막으로 반복 변수에 리스트의 마지막 요소가 할당되고 코드블록이 실행
``` python
items = ['apple', 'banana', 'coconut']

for item in items:
    print(item)
# apple
# banana
# coconut
```
> 문자열 순회
``` python
country = 'Korea'

for char in country:
    print(char)
# K
# o
# r
# e
# a
```
> range(n)
``` python
for i in range(5):
    print(i)
# 0
# 1
# 2
# 3
# 4
```
> dict()
``` python
my_dict = {
    'x': 10,
    'y': 20,
    'z': 30,
}

for key in my_dict:
    print(key)
    print(my_dict[key])
# x
# 10
# y
# 20
# z
# 30
```

> len()을 이용한 순회
``` python
numbers = [4, 6, 10, -8, 5]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers) # [8, 12, 20, -16, 10]
```
> 중첩된 반복문 1
``` python
outers = ['A', 'B']
inners = ['c', 'd']

for outer in outers:
    for inner in inners:
        print(outer, inner)
# A c
# A d
# B c
# B d
```
> 중첩된 반복문 2
``` python
elements = [['A', 'B'], ['c', 'd']]

for elem in elements:
    for item in elem:
        print(item)
# A
# B
# c
# d
```
#### 5) while
---
  - 주어진 조건식이 참(True)인 동안 코드를 반복해서 실행
  - 조건식이 거짓(False)가 될 때 까지 반복
> while statement의 기본 구조
``` python
while 조건식:
  코드 블록
```
> while 문 예시
``` python
a = 0

while a < 3:
  print(a)
  a += 1

print('끝')
# 0
# 1
# 2
# 끝
```
> 사용자 입력에 따른 반복
``` python
number = int(input('양의 정수를 입력해주세요.: '))
while number <= 0:
    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')
    number = int(input('양의 정수를 입력해주세요.: '))
print('잘했습니다!')
# 양의 정수를 입력해주세요.: 0
# 0은 양의 정수가 아닙니다.
# 양의 정수를 입력해주세요.: -3
# 음수를 입력했습니다.
# 양의 정수를 입력해주세요.: 5
# 잘했습니다!
```
#### 6) while 문은 반드시 종료 조건이 필요함
---
> #### 적절한 반복문 활용하기
  - for
    - 반복 횟수가 명확하게 정해져 있는 경우에 유용
    - 예를 들어 리스트, 튜플, 문자열 등과 같은 시퀀스 형식의 데이터를 처리할 때

#### 7) 반복 제어
---
  - for문과 while은 매 반복마다 본문 내 모든 코드를 실행하지만 때때로 일부만 실행하는것이 필요할 때가 있음

> #### 반복문 제어 키워드
  - break
    - 반복을 즉시 중지
  - continue
    - 다음 반복으로 건너뜀
  - pass
    - 아무런 동작도 수행하지 않고 넘어감
``` python
# break
for i in range(10):
    if i == 5:
        break
    print(i)

# continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# pass
for i in range(10):
    pass
```
> break 예시 1
  - 프로그램 종료 조건 만들기
``` python
number = int(input('양의 정수를 입력해주세요.: '))
while number <= 0:
    if number == -9999:
        print('프로그램을 종료합니다.')
        break
    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')
    number = int(input('양의 정수를 입력해주세요.: '))
print('잘했습니다!')
# 양의 정수를 입력해주세요.: -9999
# 프로그램을 종료합니다.
# 잘했습니다!
```

> break 예시 2
``` python
numbers = [1, 3, 5, 6, 7, 9, 10, 11]
found_even = False

for number in numbers:
    if number % 2 == 0:
        print(f"첫번째 짝수 {number}를 찾았습니다.")
        found_even = True
        break
if found_even == False:
    print('짝수를 찾지 못함')
#첫번째 짝수 6를 찾았습니다.
```
> coninue 예시
``` python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 0:
        continue
    print(number)
# 1
# 3
# 5
# 7
# 9
```
> pass 예시
  - 코드 작성 중 미완성 부분
    - 구현해야 할 부분이 나중에 추가될 수 있고,
    - 코드를 컴파일하는 동안 오류가 발생하지 않음
``` python
def my_function():
  pass
```

### 8. List Comprehension
---
  - 간결하고 효율적인 리스트 생성 방법
#### 1) List Comprehension 구조
``` python
squared_numbers2 = [num**2 for num in numbers]
squared_numbers3 = list(num**2 for num in numbers)
print(squared_numbers2) # [1, 4, 9, 16, 25]
print(squared_numbers3) # [1, 4, 9, 16, 25]
```

> List Comprehension 활용 예시
  - 2차원 배열 생성 시 (인접행렬 생성 시)
``` python
data1 = [[0] * (5) for _ in range(5)]
print(data1)
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
```
#### 2) Comprehension을 남용하지 말자.
---
  - 리스트 생성이 목적이다.

### 9. 참고
> #### 모듈 내부 살펴보기
  - 내장 함수 help를 사용해 모듈에 무엇이 들어있는지 확인 가능
> #### 1) enumerate(iterable, start = 0)
  - iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수
``` python
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(f"인덱스 {index} : {fruit}")s
# 인덱스 0 : apple
# 인덱스 1 : banana
# 인덱스 2 : cherry
```