# 클래스    
    
## @classmethod와 @staticmethod    
    
### 기능 설명  
- **@classmethod**
  - 클래스 자체를 첫 번째 인자(`cls`)로 받는 메서드
  - 인스턴스가 아닌 **클래스 상태를 다루거나 생성 로직을 커스터마이징**할 때 사용
- **@staticmethod**
  - 클래스/인스턴스와 무관한 독립 함수
  - 단지 네임스페이스(클래스 내부)에 묶여 있을 뿐, 특별한 바인딩 없음

---

### 예시 코드
```python
class Example:
    count = 0

    def __init__(self):
        Example.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def add(a, b):
        return a + b

# 사용
e1 = Example()
e2 = Example()

print(Example.get_count())  # 2
print(Example.add(3, 4))    # 7
```

---

### 사용되는 상황 (중요)  
- **@classmethod**
  - "객체 생성 방식"을 다양화할 때 핵심적으로 사용됨
    ```python
    class User:
        def __init__(self, name):
            self.name = name

        @classmethod
        def from_dict(cls, data):
            return cls(data["name"])
    ```
  - 왜 유용한가?
    - 생성 로직을 `__init__`에 몰아넣으면 확장성이 떨어짐
    - classmethod는 **팩토리 메서드 패턴** 구현에 적합

- **@staticmethod**
  - 클래스와 논리적으로 관련 있지만 상태를 전혀 사용하지 않을 때
  - 예: 유효성 검사, 단순 계산 함수
  - 왜 유용한가?
    - 관련 함수들을 클래스 안에 모아 **응집도 증가**
    - 전역 함수보다 구조적으로 명확

---

## self와 cls의 정확한 이해    
    
### 기능 설명  
- **self**
  - 인스턴스 자신
  - 모든 인스턴스 메서드의 첫 번째 인자
- **cls**
  - 클래스 자신
  - classmethod에서 사용

---

### 예시 코드
```python
class Test:
    value = 10

    def instance_method(self):
        return self.value

    @classmethod
    def class_method(cls):
        return cls.value
```

---

### 사용되는 상황 (중요)  
- `self`
  - 객체의 상태를 읽거나 수정할 때
  - 즉, "객체마다 다른 값"을 다룰 때

- `cls`
  - 클래스 전체에 공통된 상태를 다룰 때
  - 상속 구조에서 특히 중요
    ```python
    class A:
        @classmethod
        def create(cls):
            return cls()

    class B(A):
        pass

    b = B.create()  # B 인스턴스 생성
    ```
  - 왜 중요한가?
    - `cls`를 사용해야 **상속 시에도 올바른 클래스가 생성됨**
    - `A()`를 직접 쓰면 다형성이 깨짐

---

## 메직 메서드들    
    
### 기능 설명  
- `__something__` 형태의 메서드
- 파이썬 내부 동작과 연결됨 (연산자, 객체 생성, 출력 등)

---

### 예시 코드
```python
class Vector:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return Vector(self.x + other.x)

    def __repr__(self):
        return f"Vector({self.x})"
```

---

### 사용되는 상황 (중요)  
- 연산자 오버로딩 (`+`, `-`, `*`)
- 객체 출력 (`print`)
- 컨테이너 동작 (`len`, `in`)
- 왜 중요한가?
  - 클래스가 **내장 타입처럼 자연스럽게 동작하게 만듦**
  - DSL(도메인 특화 언어) 구현 시 핵심

---

### `__new__`와 `__init__`의 차이    
    
### 기능 설명  
- `__new__`
  - 객체 "생성" 단계
  - 실제로 인스턴스를 반환
- `__init__`
  - 객체 "초기화" 단계
  - 이미 생성된 객체를 설정

---

### 예시 코드
```python
class MyClass:
    def __new__(cls):
        print("new 호출")
        instance = super().__new__(cls)
        return instance

    def __init__(self):
        print("init 호출")

obj = MyClass()
```

---

### 사용되는 상황 (중요)  
- `__new__`
  - **불변 객체 (int, str 등) 커스터마이징**
  - 싱글톤 패턴
    ```python
    class Singleton:
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance
    ```
  - 왜 중요한가?
    - 객체 생성 자체를 제어할 수 있음

- `__init__`
  - 일반적인 속성 초기화
  - 대부분의 경우 여기만 사용

---

### `__call__`    
    
### 기능 설명  
- 객체를 함수처럼 호출 가능하게 만듦

---

### 예시 코드
```python
class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count

c = Counter()
print(c())  # 1
print(c())  # 2
```

---

### 사용되는 상황 (중요)  
- 상태를 가진 함수 객체
- 함수형 인터페이스 제공
- 예:
  - PyTorch 모델 (`model(input)`)
- 왜 유용한가?
  - 객체 + 함수의 장점을 결합
  - 전략 패턴, 콜백 구조에서 매우 강력

---

## 추상 클래스와 @property    
    
### 기능 설명  
- **추상 클래스**
  - 반드시 구현해야 하는 메서드를 정의
- **@property**
  - 메서드를 속성처럼 접근 가능하게 만듦

---

### 예시 코드
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "멍멍"

class Person:
    def __init__(self):
        self._age = 0

    @property
    def age(self):
        return self._age
```

---

### 사용되는 상황 (중요)  
- 추상 클래스
  - 인터페이스 강제
  - 큰 시스템에서 구조 유지
  - 왜 중요한가?
    - 구현 누락을 컴파일 단계에서 방지

- property
  - getter/setter 제어
  - 내부 구조 숨기기
  - 예:
    ```python
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError()
        self._age = value
    ```
  - 왜 중요한가?
    - 캡슐화 유지 + 인터페이스 단순화

---

## 유틸리티 클래스    
    
### 기능 설명  
- 상태 없이 함수만 모아둔 클래스

---

### 예시 코드
```python
class MathUtils:
    @staticmethod
    def square(x):
        return x * x
```

---

### 사용되는 상황 (중요)  
- 관련 함수들을 묶을 때
- 예:
  - 문자열 처리
  - 수학 연산
- 왜 중요한가?
  - 코드 구조 정리
  - 네임스페이스 충돌 방지

---

## 클래스에 적는 변수나 코드의 동작    
    
### 클래스 변수    
    
### 기능 설명  
- 클래스 수준에서 공유되는 변수

---

### 예시 코드
```python
class A:
    count = 0

    def __init__(self):
        A.count += 1
```

---

### 사용되는 상황 (중요)  
- 모든 인스턴스가 공유해야 하는 상태
- 예:
  - 생성된 객체 수
  - 설정값
- 주의:
  - mutable 객체(list, dict)는 의도치 않은 공유 발생 가능

---

### init 없이 그냥 내부에 코드를 적을 경우    
    
### 기능 설명  
- 클래스 정의 시점에 실행됨 (import 시 1회 실행)

---

### 예시 코드
```python
class A:
    print("클래스 정의 중 실행")

    x = 10
```

---

### 사용되는 상황 (중요)  
- 클래스 생성 시 초기 설정
- 메타프로그래밍
- 데코레이터/레지스트리 패턴
  ```python
  registry = {}

  class MyClass:
      registry["MyClass"] = MyClass
  ```

- 왜 중요한가?
  - 클래스 자체도 하나의 실행 블록이라는 점 이해 필요
  - import 타이밍과 강하게 연결됨

---

## 전체 구조적 관점 정리

이 개념들은 단순 기능이 아니라 아래 계층 구조로 이해하는 것이 중요하다:

- 객체 생성 단계: `__new__` → `__init__`
- 바인딩 방식:
  - 인스턴스 → `self`
  - 클래스 → `cls`
  - 독립 → staticmethod
- 인터페이스 설계:
  - 추상 클래스
  - property
- 객체 동작 확장:
  - 메직 메서드
  - call