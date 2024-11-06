

- [LAB-7 Feedback](#lab-7-feedback)
    - [Test Cases](#test-cases)
    - [Blind Test](#blind-test)
    - [Open Test](#open-test)
    - [Documents for Participation Grade](#documents-for-participation-grade)
    - [Comments on the grading](#comments-on-the-grading)
    - [Grade:](#grade)
    - [Participation Grade:](#participation-grade)

# LAB-7 Feedback

### Test Cases

Just for one run

| Test Case | in: floor type | in: length | in: width | out: room cost |
|-----------|----------------|------------|-----------|----------------|
| 1         | hardwood       | 10         | 2.5       | 34.75          |
| 2         | carpet         | 5          | 5         | 99.75          |
| 3         | tiLE           | 1          | 3         | 14.97          |
| 4         | tile           | 0          | 2         | 0              |
| 5         | Carpet         | 15.3       | 4         | 244.188        |
|     -     |         -      |      -     |Total      | 393.658        |

### Blind Test

| Result   | Description                                                              |
|----------|--------------------------------------------------------------------------|
| **YES-** | States purpose of program at start                                      |
| **YES-** | Prompts are clear                                                        |
| **YES-** | Asks for a flooring choice for each of 5 rooms                          |
| **YES-** | Asks for length and width for each of 5 rooms                           |
| **YES-** | Asks for all input for a particular room before asking for input on the next room |
| **-NO** | Correct calculation for overall total in test case                      |
| **-NO** | Correct calculation for first 2 rooms in test case                      |
| **-NO** | Correct calculation for room 3 in test case (capitalization check)      |
| **-NO** | Correct calculation for room 4 in test case (0 dimension check)         |
| **-NO** | Correct calculation for room 5 in test case (another carpet option)     |
| **-NO** | Outputs cost of each individual room and total cost across all 5 rooms  |
| **-NO** | If negative value given for width or length, continues asking until valid input given |
| **YES-NO** | If invalid floor option given, continues asking until valid option given |

### Open Test
| Result     | Description                                                              |
|------------|--------------------------------------------------------------------------|
| **NO-** | The algorithm matches the code                                           |
| **YES-** | There is a block of introductory comments at the top                    |
| **YES-** | Purpose of the program is clearly stated |  
| **YES-** | There are comments in the body of the code (do not need to determine if they are good) |
| **YES-** | Each function has introductory comments                                 |
| **YES-** | Code uses `.lower()` or `.upper()` on the flooring choice               |



### Documents for Participation Grade

|Result         |Type            |
|---------------|----------------|
|**-NO** | Reflection 1   |
|**YES-** | Reflection 2   |
|**YES-** | Algorithm      |
|**YES-** | test cases      |

### Comments on the grading
- Does not work for float type
- Seting floor type cost outside in the algorithm and inside in the code
- 
### Grade: R

### Participation Grade: S
U for hazel for using a different key of encription
 - If participation grade is unsatisfactory check the `NO` in the documents sections
