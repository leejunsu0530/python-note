# python-note 

## typings

### TypeDict

### dataclass

### 인자를 유지하는 형태

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
