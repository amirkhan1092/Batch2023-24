### Problem Statement:
Design an algorithm for an ATM machine that dispenses currency notes of denominations ₹2000, ₹500, ₹200, and ₹100. The goal is to minimize the number of notes dispensed for any withdrawal. **At least one ₹100 note is compulsory** in every transaction.

#### Constraints:
1. The withdrawal amount must be a multiple of ₹100.
2. The minimum withdrawal amount is ₹100.
3. The output should specify the number of each type of note (₹2000, ₹500, ₹200, ₹100) to be dispensed.

### Input:
- An integer `amount` representing the withdrawal amount.

### Output:
- The minimum number of notes to withdraw the exact amount. If the amount is invalid, return an error message.
- The output should include the count of ₹2000, ₹500, ₹200, and ₹100 notes.

---

### Sample Input and Output:

#### Example 1:
**Input:**
```
4600
```
**Output:**
```
₹2000: 2, ₹500: 1, ₹200: 0, ₹100: 2
```

Explanation:
- Total withdrawal amount: ₹4600
- 2 notes of ₹2000 = ₹4000
- 1 note of ₹500 = ₹500
- 1 compulsory ₹100 note + 1 additional ₹100 note = ₹200
- Total: ₹4000 + ₹500 + ₹200 = ₹4600

#### Example 2:
**Input:**
```
3700
```
**Output:**
```
₹2000: 1, ₹500: 3, ₹200: 1, ₹100: 1
```

Explanation:
- Total withdrawal amount: ₹3700
- 1 note of ₹2000 = ₹2000
- 3 notes of ₹500 = ₹1500
- 1 note of ₹200 = ₹200
- 1 compulsory ₹100 note = ₹100
- Total: ₹2000 + ₹1500 + ₹200 + ₹100 = ₹3700

#### Example 3:
**Input:**
```
250
```
**Output:**
```
Invalid amount. Must be a multiple of ₹100 and at least ₹100.
```

Explanation:
- The amount is less than ₹100 or not a multiple of ₹100, so it's invalid for withdrawal.

#### Example 4:
**Input:**
```
4100
```
**Output:**
```
₹2000: 2, ₹500: 0, ₹200: 1, ₹100: 3
```

Explanation:
- Total withdrawal amount: ₹4100
- 2 notes of ₹2000 = ₹4000
- 1 note of ₹200 = ₹200
- 1 compulsory ₹100 note + 2 additional ₹100 notes = ₹300
- Total: ₹4000 + ₹200 + ₹300 = ₹4100
