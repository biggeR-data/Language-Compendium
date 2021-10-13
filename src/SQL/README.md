# SQL

## ToC
1. [Getting Started](https://github.com/Big-P/Language-Compendium/tree/main/src/SQL#getting-started)
2. [Select](https://github.com/Big-P/Language-Compendium/tree/main/src/SQL#select)
3. [Filtering](https://github.com/Big-P/Language-Compendium/tree/main/src/SQL#filtering)
4. [Aggregation](https://github.com/Big-P/Language-Compendium/tree/main/src/SQL#aggregation)
5. [Sorting](https://github.com/Big-P/Language-Compendium/tree/main/src/SQL#sorting)
6. [Naming](https://github.com/Big-P/Language-Compendium/tree/main/src/SQL#naming)
7. [Calculation](https://github.com/Big-P/Language-Compendium/tree/main/src/SQL#calculation)
8. [Unions](https://github.com/Big-P/Language-Compendium/tree/main/src/SQL#unions)
9. [Joins](https://github.com/Big-P/Language-Compendium/tree/main/src/SQL#joins)

---

<br>

## Getting started

<br>

### **Setup**

<br>

First we need to setup some exemplary data.

> We create a scheme named ```ex```. <br>

```sql
CREATE SCHEMA ex;

# targets our schema as the default schema for the following statements
USE ex;
```

*if you want to delete the schema you need to use ```DROP SCHEMA```*

> After that we create the following Tables: <br>
> *Hint: Use this [site](https://tableconvert.com/) to convert Markdown Tables to SQL Table Creation*


exemplary table creation:
```sql
CREATE TABLE "schema"."table1" (
    Attribute1 INT DEFAULT 1,
    Attribute2 VARCHAR(20) NOT NULL,
    CONSTRAINT "constraint-name" FOREIGN KEY(Attribute1) REFERENCES table2(relatedAttributed)
    PRIMARY KEY(Attribute1, Attribute2),
    UNIQUE KEY(Attribute2)
)
```

<br>

Table: Customer
| CustomerID | Name     | Location   | Credit_score |
|------------|----------|------------|--------------|
| C1         | Smith    | London     | 55           |
| C2         | Williams | Manchester | 23           |
| C3         | Jones    | Liverpool  | 23           |
| C4         | Wilson   | London     | 54           |
| C5         | Brown    | Birmingham | 43           |
| C6         | Evans    | Cambridge  | 10           |

<br>

Table: Article
| ArcticleID | Tag      | Price |
|------------|----------|-------|
| A1         | Computer | 1000  |
| A2         | Stereo   | 500   |
| A3         | TV       | 1500  |
| A4         | Camera   | 200   |

<br>

Table: Branch
| BranchID | Location   |
|----------|------------|
| B1       | London     |
| B2       | Birmingham |
| B3       | Glasgow    |

<br>

Table: Transaction
| CustomerID | ArticleID | BranchID | Quantity | Date       |
|------------|-----------|----------|----------|------------|
| C1         | A1        | B1       | 4        | 10.01.2006 |
| C1         | A2        | B1       | 2        | 10.01.2006 |
| C1         | A3        | B2       | 1        | 11.02.2006 |
| C2         | A1        | B3       | 5        | 22.03.2006 |
| C2         | A2        | B1       | 1        | 22.02.2006 |
| C2         | A2        | B1       | 1        | 22.02.2006 |
| C2         | A4        | B3       | 2        | 11.03.2006 |
| C3         | A1        | B2       | 5        | 08.04.2006 |
| C3         | A3        | B2       | 2        | 08.04.2006 |
| C3         | A4        | B1       | 3        | 29.04.2006 |
| C4         | A1        | B2       | 3        | 22.03.2006 |
| C4         | A2        | B3       | 1        | 25.03.2006 |
| C5         | A3        | B3       | 1        | 14.01.2006 |
| C5         | A4        | B3       | 2        | 04.02.2006 |
| C6         | A2        | B3       | 2        | 25.03.2006 |

> Adding rows:
```sql
INSERT INTO "schema"."Table" ("Attribute1", "Attribute2") VALUES("Attr1-Value", "Attr2-Value");
```

---

<br>

# The Essentials

<br>

## Select

<br>

### **All Attributes - Asterisk selector**
```sql
SELECT * FROM ex.Article;
```
> returns the entire Article Table

<br>

### **Selected Attributes**
```sql
SELECT ArticleID, Price FROM ex.Article;
```
> returns the Article Table without the Tag column

<br>

### **Duplicate removal - DISTINCT Statement**
```sql
SELECT DISTINCT Location FROM ex.Customer;
```

---

<br>

## Filtering

<br>

### **Operators**
> <, >, <=, >=, =, !=

<br>

### **Boolean Comparisons**
> ```IS```, ```NOT```, ```AND```, ```OR```
```sql
SELECT * FROM ex.Transaction WHERE NOT Quantity = 3;
```

<br>

### **Set**
```sql
SELECT * FROM ex.Article WHERE Price in (100,200,300,400,500);
```
> returns Articles that have the same Price as elements defined in the provided set

<br>

### **Border Constraints**
```sql
SELECT * FROM ex.Article WHERE Price BETWEEN 100 AND 1000;
```
> returns all Articles with a Price in the range of 100 and 1000 <br>
> *Hint: Both of the borders are inclusive*

<br>

### **Textual Pattern Matching**

> % - any character - length: 0-n <br>
> _ - any character - length: 1 (-> Wildcard)

```sql
SELECT * FROM ex.Branch WHERE Location LIKE "%o_";
```

| BranchID | Location   |
|----------|------------|
| B1       | London     |
| B3       | Glasgow    |

<br>

### **Chaining Comparisons**
```sql
SELECT * FROM ex.Customer WHERE Wohnort="London" AND Credit_score > 54;
```

| CustomerID | Name     | Location   | Credit_score |
|------------|----------|------------|--------------|
| C1         | Smith    | London     | 55           |

---

<br>

## Aggregation

> can only be used in ```SELECT``` or ```HAVING``` not with ~~```WHERE```~~

<br>

### **Counting with COUNT**
```sql
SELECT COUNT(*) AS Purchases FROM ex.Transaction;
```
> returns the overall count of records -> 15

```sql
SELECT COUNT(DISTINCT CustomerID) AS Customers FROM ex.Transaction;
```
> returns the count of unique customer records -> 6 <br>
> **NULLs are counted**

<br>

### **Counting with SUM**
```sql
SELECT SUM(Quantity) FROM ex.Transaction WHERE CustomerID="C1";
```
> Sums up the count of transactions for a customer -> 7

<br>

### **Minimums, Maximums and Averages**
> ```MIN```, ```MAX```, ```AVG``` keywords
```sql
SELECT MAX(Quantity) FROM ex.Transaction;
```
> returns 5 (*not multiple even though there are multiple fives*)

<br>

### **Filtering combined with Aggregation GROUP BY & HAVING keywords**
```sql
SELECT BranchID, SUM(Quantity) FROM ex.Transaction GROUP BY BranchID HAVING COUNT(*) >= 5;
```
> ```GROUP BY``` groups same IDs together, ```HAVING``` filters after grouping <br>
> *```WHERE``` filters before grouping*

| BranchID | Quantity |
|----------|----------|
| B1       | 11       |
| B3       | 13       |


---

<br>

## Sorting

<br>

### **Ascending and Descending Values**
> ```ASC```, ```DESC```
```sql
SELECT * FROM ex.Customer ORDER BY Location, Credit_score DESC;
```
> if no order is specified ```ASC``` is the default choice <br>
> First the Location is ordered, then for same Locations it is sorted by the descending credit score

| CustomerID | Name     | Location   | Credit_score |
|------------|----------|------------|--------------|
| C5         | Brown    | Birmingham | 43           |
| C6         | Evans    | Cambridge  | 10           |
| C3         | Jones    | Liverpool  | 23           |
| C1         | Smith    | London     | 55           |
| C4         | Wilson   | London     | 54           |
| C2         | Williams | Manchester | 23           |

---

<br>

## Naming

<br>

### **renaming Attributes - AS Keyword**
```sql
SELECT BranchID AS ID_Branch FROM ex.Branch;
```
| ID_Branch | Location   |
|-----------|------------|
| B1        | London     |
| B2        | Birmingham |
| B3        | Glasgow    |

---

<br>

## Calculation

<br>

### **Calculating a column based on another column**
```sql
SELECT 
    Price,
    Price*0.5 AS Sale
FROM ex.Article;
```
| Price | Sale |
|-------|------|
| 1000  | 500  |
| 500   | 250  |
| 1500  | 750  |
| 200   | 100  |

---

<br>

## Unions

> Unions are by default ```DISTINCT```, so there is no need to write ~~```UNION DISTINCT```~~ <br>
> ```UNION ALL``` includes duplicates

```sql
SELECT Location FROM ex.Branch
UNION
SELECT Location from ex.Customer;
```
| Location   |
|------------|
| London     |
| Birmingham |
| Glasgow    |
| Manchester |
| Liverpool  |
| Cambridge  |

---

<br>

## Joins

> ```FROM``` contains the tables which are joined <br>
> ```WHERE``` states the base of the join which is usually the foreign key corresponding to the primary key of one of the tables <br>
> > if none is provided you receive the Cartesian Product (A x B)
```sql
SELECT * FROM ex.Branch, ex.Customer;
```

JOIN Options:
> [] optional keywords <br>
> ```[NATURAL] [INNER] JOIN``` <br>
> ```[NATURAL] LEFT [OUTER] JOIN``` <br>
> ```[NATURAL] RIGHT [OUTER] JOIN``` <br>
> ```[NATURAL] FULL [OUTER] JOIN```

*Hint: including INNER and OUTER doesn't change the outcome*

<br>

### **Equi/Self Joins**
```sql
SELECT * FROM ex.Branch, ex.Customer WHERE Location = Location;
```

| CustomerID | Name     | Location   | Credit_score | BranchID |
|------------|----------|------------|--------------|----------|
| C1         | Smith    | London     | 55           | B1       |
| C4         | Wilson   | London     | 54           | B1       |
| C5         | Brown    | Birmingham | 43           | B2       |

> Alternatively the JOIN could be achieved in the FROM statement
```sql
SELECT * FROM ex.Branch JOIN ex.Customer ON Branch.Location = Customer.Location;
```

> Conditions can be added in the ```WHERE``` part with the usage of ```AND``` (eg. AND X < Y) <br>
> Multiple joins are possible with the usage of ```AND``` followed by another join (eg. X = X and Y = Y)

<br>

### **Join by explicit same Attribute names - JOIN USING**
```sql
SELECT DISTINCT Name
FROM ex.Customer    JOIN ex.Transaction USING (CustomerID)
                    JOIN ex.Article USING (ArticleID)
WHERE Tag = "Computer";
```

| Name     |
|----------|
| Smith    |
| Williams |
| Jones    |
| Wilson   |

> CustomerIDs C1, C2, C3 and C4 bought a Computer (A1), those IDs were used to obtain the corresponding ```DISTINCT``` Names

<br>

### **Join over all Attributes that share the same name - NATURAL JOIN**
```sql
SELECT DISTINCT Name
FROM ex.Customer NATURAL JOIN ex.Transaction NATURAL JOIN ex.Article
WHERE Tag = "Computer";
```

| Name     |
|----------|
| Smith    |
| Williams |
| Jones    |
| Wilson   |

<br>

### **OUTER JOIN**

> Let's suppose we have this statement given:

```sql
SELECT * FROM A <DIRECTION> JOIN B ON A.X = B.X;
```

> This table will help you understand which OUTER JOIN will cause which Attribute/record to produce NULLs

|       | A    | B    |
|-------|------|------|
| LEFT  | All  | NULL |
| RIGHT | NULL | All  |
| FULL  | All* | All* |

> All - contains all values of said Attribute <br>
> NULL - contains NULLs when there is no match of said Attribute <br>
> All* - contains all values of said Attribute, however there is also the possibility to receive NULLs depending on your records

<br>

### LEFT/RIGHT
```sql
SELECT *
FROM ex.Customer 
    LEFT JOIN ex.Branch ON Customer.Location = Branch.Location;
```

| CustomerID | Name     | Location   | Credit_score | BranchID |
|------------|----------|------------|--------------|----------|
| C1         | Smith    | London     | 55           | B1       |
| C2         | Williams | Manchester | 23           | NULL     |
| C3         | Jones    | Liverpool  | 23           | NULL     |
| C4         | Wilson   | London     | 54           | B1       |
| C5         | Brown    | Birmingham | 43           | B2       |
| C6         | Evans    | Cambridge  | 10           | NULL     |

<br>

### FULL

> **not supported by MySQL**

```sql
SELECT *
FROM ex.Customer
    FULL JOIN ex.Branch ON Customer.Location = Branch.Location;
```

| CustomerID | Name     | Location   | Credit_score | BranchID |
|------------|----------|------------|--------------|----------|
| C1         | Smith    | London     | 55           | B1       |
| C2         | Williams | Manchester | 23           | NULL     |
| C3         | Jones    | Liverpool  | 23           | NULL     |
| C4         | Wilson   | London     | 54           | B1       |
| C5         | Brown    | Birmingham | 43           | B2       |
| C6         | Evans    | Cambridge  | 10           | NULL     |
| NULL       | NULL     | Glasgow    | NULL         | B3       |

---