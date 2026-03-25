# python-note 

## typings

## Enum

### TypeDict

### dataclass

### 인자를 유지하는 형태의 타이핑

## 바다코끼리 연산자

## if문, for else문

```python
i = input()
if i == "1":
    pass
if i == "2":
    pass
```

여기서 if만 적으면 독립적이게 된다. 어처피 각각 다른걸 감지하면 상관없겠지만, 뒤 조건 검사에 리소스가 들어는 가니까 그냥 2번째부터 elif 쓰는 게 낫다. 가독성이나 의도도 명확하다.

## 클래스
여기 이하는 각각의 사용례도 첨부한다.

### @classmethod와 @staticmethod

### `__new__`와 `__init__`의 차이

### 추상 클래스와 @property

### 유틸리티 클래스

### 클래스에 적는 변수나 코드의 동작