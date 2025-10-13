# ⚙️ The Eval Function（求值函数）详解

## 一、核心概念

> The **eval function** computes the value of an expression.

它是整个解释器的“核心大脑”，负责**把语法树（表达式结构）计算成实际结果**。  
换句话说，`calc_eval` 是“执行表达式”的函数。

---

## 二、基本定义

```python
def calc_eval(exp):
    if type(exp) in (int, float):
        return exp
    elif isinstance(exp, Pair):
        arguments = exp.second.map(calc_eval)
        return calc_apply(exp.first, arguments)
    else:
        raise TypeError
```

### ✳️ 功能总结
- 根据表达式的类型（数字 or 调用表达式）采取不同处理。
- 对嵌套结构递归求值。
- 委托 `calc_apply` 执行最终运算。

---

## 三、工作流程解析

### 1️⃣ 数字表达式（Primitive Expression）

```python
if type(exp) in (int, float):
    return exp
```
- 如果 `exp` 是数字，直接返回自己。
- 因为数字的值就是它自身。

🧩 对应语言语义：  
> A number evaluates to itself.

---

### 2️⃣ 调用表达式（Call Expression）

```python
elif isinstance(exp, Pair):
    arguments = exp.second.map(calc_eval)
    return calc_apply(exp.first, arguments)
```
- `exp.first` → 操作符（operator），例如 `'+'`, `'*'` 等。
- `exp.second` → 参数（operands）的列表。
- 递归调用 `calc_eval` 对每个参数求值。
- 将求得的参数值传入 `calc_apply`，执行实际运算。

🧩 对应语言语义：  
> A call expression evaluates to its argument values combined by an operator.

---

### 3️⃣ 错误处理

```python
else:
    raise TypeError
```
- 若既不是数字，也不是调用表达式 → 抛出异常。

---

## 四、执行过程举例

### 示例表达式
```
(* (+ 2 3) 4)
```

### 结构（Pair 表示）
```
Pair('*', Pair(Pair('+', Pair(2, Pair(3, nil))), Pair(4, nil)))
```

### 求值步骤
1. `calc_eval` 看到 `*` → 是调用表达式  
2. 递归计算第一个参数 `(+ 2 3)`  
   - 进一步递归得到 2、3 → 调用 `calc_apply('+', [2,3])` → 5  
3. 第二个参数 4 → 直接返回  
4. 调用 `calc_apply('*', [5,4])` → 得 20  

✅ 最终结果：`20`

---

## 五、`calc_apply` 函数（运算执行）

虽然幻灯片中未展示，但其典型定义如下：

```python
def calc_apply(operator, args):
    if operator == '+':
        return sum(args)
    elif operator == '-':
        return reduce(lambda x, y: x - y, args)
    elif operator == '*':
        return reduce(lambda x, y: x * y, args)
    elif operator == '/':
        return reduce(lambda x, y: x / y, args)
```

- 负责根据操作符执行对应数学运算。
- 输入是操作符和参数值列表。

---

## 六、Language Semantics（语言语义）

| 表达式类型 | 求值语义 |
|-------------|------------|
| **Number** | 自身即为其值 |
| **Call Expression** | 对每个参数递归求值，然后用操作符组合这些值 |

这定义了解释器的“语义规则” —— 语言是如何被计算的。

---

## 七、与前几页的联系

| 前一页 | 内容 | 本页作用 |
|---------|------|----------|
| **Calculator Syntax** | 定义了表达式的结构（数字/调用） | `calc_eval` 负责计算这些结构的结果 |
| **Syntactic Analysis** | 构建语法树 | `calc_eval` 遍历语法树进行求值 |
| **Parsing** | 将文本转成结构化表达式 | `calc_eval` 读取结构化表达式并执行计算 |

> Eval 是解释器的核心逻辑：让结构“动起来”。

---

## ✅ 总结

- `calc_eval` 是解释器中“求值”的核心函数。
- 它的本质是一种**递归定义**：
  - 数字 → 返回自己。
  - 调用 → 先求参数，再组合计算。
- `calc_apply` 是辅助执行器，负责真正的数学运算。
- 这体现了解释器最根本的原则：
  > **Eval is the heart of interpretation.**

---

## 🧩 一句话总结

> **`calc_eval` 让静态的语法结构变成可执行的计算过程。**
