# Журнал TDD (красный → зелёный)

Файл сгенерирован автоматически: для каждой пары коммитов тесты запускались
командой `python -m unittest tests.<модуль>` на коммите с тестами (до реализации)
и на следующем коммите с реализацией.

## tests/test_student.py

### `d087d0f` — test: add failing tests for Student class

```text
ImportError: Failed to import test module: test_student
ModuleNotFoundError: No module named 'student'
Ran 1 test in 0.001s
FAILED (errors=1)
```

### `35e1fbe` — feat: add Student class with info output

```text
Ran 9 tests in 0.001s
OK
```


## tests/test_counter.py

### `13e3282` — test: add failing tests for Counter class

```text
ImportError: Failed to import test module: test_counter
ModuleNotFoundError: No module named 'counter'
Ran 1 test in 0.000s
FAILED (errors=1)
```

### `a8af949` — feat: add Counter class with bounds

```text
Ran 6 tests in 0.001s
OK
```


## tests/test_float_range.py

### `c227b4a` — test: add failing tests for FloatRange iterator

```text
ImportError: Failed to import test module: test_float_range
ModuleNotFoundError: No module named 'float_range'
Ran 1 test in 0.000s
FAILED (errors=1)
```

### `c40edf8` — feat: add FloatRange iterator class

```text
Ran 6 tests in 0.001s
OK
```


## tests/test_product.py

### `4c81cea` — test: add failing tests for Product class

```text
ImportError: Failed to import test module: test_product
ModuleNotFoundError: No module named 'shop'
Ran 1 test in 0.000s
FAILED (errors=1)
```

### `4524bf4` — feat: add Product class with decimal price

```text
Ran 4 tests in 0.001s
OK
```


## tests/test_cart_order.py

### `4df151c` — test: add failing tests for Cart and Order

```text
ImportError: Failed to import test module: test_cart_order
ImportError: cannot import name 'Cart' from 'shop' (shop.py)
Ran 1 test in 0.000s
FAILED (errors=1)
```

### `affde27` — feat: add Cart and Order classes

```text
Ran 12 tests in 0.002s
OK
```
