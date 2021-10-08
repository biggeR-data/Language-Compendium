# SQL

## ToC
1. [Getting Started](https://github.com/Big-P/Language-Compendium/tree/SQL-DB1-Script-Sync/src/SQL#getting-started)
2. [Select](https://github.com/Big-P/Language-Compendium/tree/SQL-DB1-Script-Sync/src/SQL#select)
3. [Naming](https://github.com/Big-P/Language-Compendium/tree/SQL-DB1-Script-Sync/src/SQL#naming)
4. [Calculation](https://github.com/Big-P/Language-Compendium/tree/SQL-DB1-Script-Sync/src/SQL#calculation)

---

## Getting started
### **Setup**
First we need to setup some exemplary data.

> We create a scheme named ```ex```. <br>
> After that we create the following Tables: <br>
> *Hint:Use this [site](https://tableconvert.com/) to convert Markdown Tables to SQL Table Creation*

---

Table: Customer
| CustomerID | Name     | Location   | Credit_score |
|------------|----------|------------|--------------|
| C1         | Smith    | London     | 55           |
| C2         | Williams | Manchester | 23           |
| C3         | Jones    | Liverpool  | 23           |
| C4         | Wilson   | London     | 54           |
| C5         | Brown    | Birmingham | 43           |
| C6         | Evans    | Cambridge  | 10           |

---

Table: Article
| ArcticleID | Tag      | Price |
|------------|----------|-------|
| A1         | Computer | 1000  |
| A2         | Stereo   | 500   |
| A3         | TV       | 1500  |
| A4         | Camera   | 200   |

---

Table: Branch
| BranchID | Location   |
|----------|------------|
| B1       | London     |
| B2       | Birmingham |
| B3       | Liverpool  |

---

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

---

# The Essentials

## Select

### **All Attributes - Asterisk selector**
```sql
SELECT * FROM ex.Article;
```
> returns the entire Article Table

### **Selected Attributes**
```sql
SELECT ArticleID, Price FROM ex.Article;
```
> returns the Article Table without the Tag column

### **Duplicate removal - DISTINCT Statement**
```sql
SELECT DISTINCT Location FROM ex.Customer;
```

---

## Filtering with constraints - the WHERE keyword

- [ ] Keyword HAVING

### **Operators**
> <, >, <=, >=, =, !=

### **Boolean Comparisons**
> ```IS```, ```NOT```, ```AND```, ```OR```

### **Set**
```sql
SELECT * FROM ex.Article WHERE Price in (100,200,300,400,500);
```
> returns Articles that have the same Price as elements defined in the provided set

### **Border Constraints**
```sql
SELECT * FROM ex.Article WHERE Price BETWEEN 100 AND 1000;
```
> returns all Articles with a Price in the range of 100 and 1000 <br>
> *Hint: Both of the borders are inclusive*

### **Textual Pattern Matching**

> % - any character - length: 0-n <br>
> _ - any character - length: 1 (-> Wildcard)

```sql
SELECT * FROM ex.Branch WHERE Location LIKE "L%";
```

| BranchID | Location   |
|----------|------------|
| B1       | London     |
| B3       | Liverpool  |

### **Chaining Comparisons**
```sql
SELECT * FROM ex.Customer WHERE Wohnort="London" AND Credit_score > 54;
```

| CustomerID | Name     | Location   | Credit_score |
|------------|----------|------------|--------------|
| C1         | Smith    | London     | 55           |

---

## Sorting

### **Ascending and Descending Values**
> ```ASC```, ```DESC```
```sql
SELECT * FROM ex.Customer ORDER BY Location, Credit_score DESC;
```
> if no order is specified ```ASC``` is the default choice <br>
> First the Location is order, then for same Locations it is sorted by the descending credit score

| CustomerID | Name     | Location   | Credit_score |
|------------|----------|------------|--------------|
| C5         | Brown    | Birmingham | 43           |
| C6         | Evans    | Cambridge  | 10           |
| C3         | Jones    | Liverpool  | 23           |
| C1         | Smith    | London     | 55           |
| C4         | Wilson   | London     | 54           |
| C2         | Williams | Manchester | 23           |

---

## Naming

### **renaming Attributes - AS Keyword**
```sql
SELECT BranchID AS ID_Branch FROM ex.Branch;
```
| ID_Branch | Location   |
|-----------|------------|
| B1        | London     |
| B2        | Birmingham |
| B3        | Liverpool  |

---

## Calculation

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