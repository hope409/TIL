# 데이터구조 2
## 비시퀀스 데이터 구조
### 1. 딕셔너리
---
  - 고유한 항목(key)들의 정렬되지 않은 컬렉션
#### 1) 딕셔너리 메서드
---
#### .clear()
---
  - 딕셔너리의 모든 키/값 쌍을 제거
``` python
person = {'name': 'Alice', 'age': 25}
person.clear()
print(person) # {}
```
#### .get(key[,default])
---
  - 키 연결된 값을 반환하거나 키가 없으면 None 혹은 기본 값을 반환
  - 즉 실행이 중지되지 않는다.
``` python
person = {'name': 'Alice', 'age': 25}
print(person.get('name')) # Alice
print(person.get('country')) # None
print(person.get('country', 'Unknown')) # Unknown
print(person['country']) # KeyError: 'country'
```
#### .keys()
---
  - 딕셔너리 키를 모은 객체를 반환
``` python
person = {'name': 'Alice', 'age': 25}
print(person.keys()) # dict_keys(['name', 'age'])
for item in person.keys():
    print(item) # name
                # age
```
> dict_keys, map object 등 유사한 애들이 있다.
#### .values()
---
  - 딕셔너리 값을 모은 객체를 반환
``` python
person = {'name': 'Alice', 'age': 25}
print(person.values()) # dict_values(['Alice', 25])
for item in person.values():
    print(item) # Alice
                # 25
```
#### .items
---
  - 딕셔너리 키/값 쌍을 모은 객체를 반환
``` python
person = {'name': 'Alice', 'age': 25}
print(person.items()) # dict_items([('name', 'Alice'), ('age', 25)])
for key, value in person.items():
    print(key, value) # name Alice
                      # age 25
```
#### .pop(key[,default])
---
  - 키를 제거하고 연결됐던 값을 반환 (없으면 에러나 default 를 반환)
``` python
person = {'name': 'Alice', 'age': 25}
print(person.pop('age')) # 25
print(person) # {'name': 'Alice'}
print(person.pop('country', None)) # None
print(person.pop('country')) # KeyError: 'country'
```
#### .setdefault(key[,default])
---
  - 키와 연결된 값을 반환
  - 키가 없다면 default와 연결한 키를 딕셔너리에 추가하고 default를 반환
``` python
person = {'name': 'Alice', 'age': 25}
print(person.setdefault('country', 'KOREA')) # KOREA
print(person) # {'name': 'Alice', 'age': 25, 'country': 'KOREA'}
```
#### .update([other])
---
  - other가 제공하는 키/값 쌍으로 딕셔너리를 갱신
  - 기존 키는 덮어 씀
  - 추가한다고 생각해도 될까요?
``` python
person = {'name': 'Alice', 'age': 25}
other_person = {'name': 'Jane', 'gender': 'Female'}

person.update(other_person)
print(person) # {'name': 'Jane', 'age': 25, 'gender': 'Female'}

person.update(age=50, country='KOREA')
print(person) # {'name': 'Jane', 'age': 50, 'gender': 'Female', 'country': 'KOREA'}
```
### 2. 세트
---
  - 고유한 항목들의 정렬되지 않은 컬렉션
#### 1) 세트 메서드
---
#### .add(x)
---
  - 세트에 x를 추가
``` python
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.add(4)
print(my_set) # {'a', 1, 2, 3, 'c', 'b', 4}

my_set.add(4)
print(my_set) # {1, 2, 3, 'b', 4, 'c', 'a'}
```
#### .clear()
---
  - 세트의 모든 항목을 제거
``` python
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.clear()
print(my_set) # set()
```
#### .remove(x)
---
  - 세트에서 항목 x를 제거
``` python
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.remove(2)
print(my_set) # {1, 3, 'a', 'b', 'c'}
my_set.remove(10) # KeyError: 10
```
#### .pop()
---
  - 세트에서 임의의 요소를 제거하고 반환
``` python
my_set = {'a', 'b', 'c', 1, 2, 3}
element = my_set.pop()
print(element) # 실행시 마다 다름 / 원소는 5개가 출력
```
#### .discard()
---
  - 세트 s에서 항목 x를 제거. remove와 달리 에러 없음
``` python
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.discard(2)
print(my_set) # {1, 3, 'a', 'b', 'c'}
print(my_set.discard(10)) # None
```
#### .update(iterable)
---
  - 세트에 다른 iterable 요소를 추가
``` python
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.update([1, 4, 5])
print(my_set) # {1, 2, 3, 4, 5, 'a', 'b', 'c'}
```
#### 2) 세트의 집합 메서드
---
|메서드|설명|연산자|
|:---:|:---:|:---:|
|set1.difference(set2)|set1에는 들어있지만 set2에는 없는 항목으로 세트를 생성 후 반환|set1 - se2|
|set1.intersection(set2)|set1과 set2 모두 들어있는 항목으로 세트를 생성 후 반환|set1 & set2|
|set1.issubset(set2)|set1의 항목이 모두 set2에 들어있으면 True를 반환|set1 <= set2|
|set1.issuperset(set2)|set1가 set2의 항목을 모두 포함하면 True를 반환|set1 >= set2|
|set1.union(set2)|set1 또는 set2에(혹은 둘 다) 들어있는 항목으로 세트를 생성 후 반환|set1 \| set2|

> 집합 메서드 예시
``` python
# 집합 메서드
set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}
set3 = {0, 1}

print(set1.difference(set2)) # {0, 2, 4}
print(set1.intersection(set2)) # {1, 3}
print(set1.issubset(set2)) # False
print(set3.issubset(set1)) # True
print(set1.issuperset(set2)) # False
print(set1.union(set2)) # {0, 1, 2, 3, 4, 5, 7, 9}
```
### 3. 해시 테이블
---
  - 해시 함수를 사용하여 변환한 값을 색인(index)으로 삼아 키(key)와 데이터(value)를 저장하는 자료구조
  - 데이터를 효율적으로 저장하고 검색하기 위해 사용
#### 1) 해시 테이블 원리
---
  - 키를 해시 함수를 통해 해시 값으로 변환하고, 이 해시 값을 인덱스로 사용하여 데이터를 저장하거나 검색
    - 데이터 검색이 매우 빠르게 이루어짐
#### 2) 해시(Hash)
---
  - 임의의 크기를 가진 데잍어를 고정된 크기의 고유한 값으로 변환하는것
  - 이렇게 생성된 고유한 값은 주로 해당 데이터를 식별하는 데 사용될 수 있음
    - 일정의 "지문"과 같은 역할
    - 데이터를 고유하게 식별
  - 파이썬에서는 해시 함수를 사용하여 데이터를 해시 값으로 변환하며, 이 해시 값은 정수로 표현됨
#### 3) 해시 함수(Hash function)
---
  - 임의의 길이의 데이터를 입력 받아 고정된 길이의 데이터(해시 값)를 출력하는 함수
  - 주로 해시 테이블 자료구조에 사용되며, 매우 빠른 데이터 검색을 위한 컴퓨터 소프트웨어에서 유용하게 사용
#### 4) set의 요소 & dictionary의 키와 해시테이블 관계
---
  - 파이썬에서 세트의 요소와 딕셔너리의 키는 해시 테이블을 이용하여 중복되지 않는 고유한 값을 저장함
  - 세트 내의 각 요소는 해시 함수를 통해 해시 값으로 변환되고, 이 해시 값을 기반으로 해시 테이블에 저장됨
  - 마찬가지로 딕셔너리의 키는 고유해야 하므로, 키를 해시 함수를 통해 해시 값으로 변환하여 해시 테이블에 저장
    - 따라서 딕셔너리의 키는 매우 빠른 탐색 속도를 제공하며, 중복된 값을 허용하지 않음
#### 5) 파이썬에서의 해시 함수
---
  - 파이썬에서 해시 함수의 동작 방식은 객체의 타입에 따라 달라짐
  - 정수와 문자열은 서로 다른 타입이며, 이들의 해시 값을 계산하는 방식도 다름
#### 파이썬에서의 해시 함수 - 정수
---
- 같은 정수는 항상 같은 해시 값을 가짐
- 해시 테이블에 정수를 저장할 때 효율적인 방법
- 예를 들어, hash(1)과 hash(2)는 항상 서로 다른 해시 값을 갖지만, hash(1)은 항상 동일한 해시 값을 갖게 됨

#### 파이썬에서의 해시 함수 - 문자열
---
  - 문자열은 가변적인 길이를 갖고 있고, 문자열에 포함된 각 문자들의 유니코드 코드 포인트 등을 기반으로 해시값을 계산
  - 이로 인해 문자열의 해시 값은 실행 시 마다 다르게 계산됨
> 예시 코드
``` python
my_str_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}

print(hash(1)) # 1
print(hash(1)) # 1
print(hash('a')) # 실행시마다 다름
print(hash('a')) # 실행시마다 다름
```
#### set의 pop 메서드의 결과와 해시 테이블의 관계
---
  - pop()의 set에서 임의의 요소를 제거하고 반환
  - 실행할 때마다 다른 요소를 얻는다는 의미에서의 "무작위"가 아니라
  - "임의"라은 의미에서 "무작위"
    - By "arbitrary" the docs don't mean "random"
  - 해시 테이블에 나타나는 순서대로 반환하는 것

> 1. 그렇다면 정수의 경우 순서가 정해지는 건 처음 만들어질때 정해지는 것인가??
> 2. 엄청나게 많은 숫자 경우의 수가 존재하고 문자열이 1개만 남아있다면?
>     그 문자열은 항상 같은 위치에 존재할까?

#### hashable
---
  - hash() 함수의 인자로 전달해서 결과를 반환 받을 수 있는 객체
  - 대부분의 불변형 데이터 타입은 hashable
  - 단, tuple의 경우 불변형이지만 해시 불가능한 객체를 참조 할 때는 tuple자체도 해시 불가능해짐
#### hashable과 불변성 간의 관계
---
  - 해시 테이블의 키는 불변해야 함
    - 객체가 생성된 후에 그 값을 변경할 수 없어야 함
  - 불변 객체는 해시 값이 변하지 않으므로 동일한 값에 대해 일관된 해시 값을 유지할 수 있음
  - 단, "hash 가능하다 != 불변하다"
#### 가변형 객체가 hashable 하지 않은 이유
---
  - 값이 변경될 수 있기 때문에 동일한 객체에 대한 해시 값이 변경될 가능성이 있음(해시 테이블의 무결성 유지 불가)
  - 가변형 객체가 변경되면 해시 값이 변경되기 때문에, 같은 객체에 대한 서로 다른 해시 값이 반환될 수 있음(해시 값의 일관성 유지 불가)
#### hashable 객체가 필요한 이유
---
1. 해시 테이블 기반 자료 구조 사용
   - set와 dict의 key
   - 중복 값 방지
   - 빠른 검색과 조회
2. 불변성을 통한 일관된 해시 값
3. 안정성과 예측 가능성 유지
### 4. 파이썬 문법 규격
---
   - 파이썬 공식문서 확장 BNF 표기법
#### 1) BNF
---
   - "Backus-Naur Form"
   - 프로그래밍 언어의 문법을 표현하기 위한 표기법
#### 2) EBNF
---
   - "extended Backus-Naur Form"
   - BNF를 확장한 표기법
   - 메타 기호를 추가하여 더 간결하고 표현력이 강해진 형태
> 대표적인 EBNF 메타기호

|메타 기호|의미|
|:---:|:---:|
|[]|선택적 요소|
|{}|0번 이상 반복|
|()|그룹화|

#### EBNF 메타기호 [] 사용 예시
---
   - 딕셔너리의 pop 메서드
   - pop(key[, default])

#### BNF와 같은 표기법을 사용하는 이유
---
   - 서로 다른 프로그래밍 언어, 데이터 형식, 프로토콜 등의 문법을 통일하여 정의하기 위함