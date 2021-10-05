# Python-Docu
My own personal collection of Python Code. Good to knows and more.

# To-Do's
- [ ] Modules and Packaging with \_\_init__
- [X] restructuring


# General

## Strings

### **Unicode Strings**
```python
uni_string = u"This String is encoded in Unicode"
```

### **Tuple Return**
```Python
def add_sub(a,s):
    a += 1
    s -= 1
    return a,s

added, subtracted = add_sub(9,2)
# added = 10 ; subtracted = 1
```

## Dictionnaries 
```Python

```

### Reverse Dictionnaries
```Python
original_dict = {"Germany":"Central", "Swiss": "Central", "Sweden":"North", "Italy":"South"}
reversed_dict = {}
for k,v in original_dict.items():
    if v in reversed_dict:
        reversed_dict[v].append(k)
    else:
        reversed_dict[v] = [k]

# reversed_dict = {"Central":["Germany", "Swiss"], "North":["Sweden"], "South":["Italy"]}
```

## Files

### **Operations**
```python
# Reading
```

```python
# Writing
```

```python
# Appending
```

> Modes Table

# Modules

## Pandas pandas==1.2.3 & python==3.7.9

## Display Dataframe
```Python
from IPython.display import display
import pandas as pd

df = pd.Dataframe(
    "temperature": ["cold", "warm"],
    "region": ["Taiga", "Desert"]
)

display(df)
```

|   | temperature | region |
|---|-------------|--------|
| 0 | cold        | Taiga  |
| 1 | warm        | Desert |

### **Filter**
```Python

```

### **groupby**
```Python

```

## Series to Dataframe
```Python
import pandas as pd
d = {"a": 1, "b": 2, "c": 3}
series = pd.Series(data=d)
df = series.to_frame()
```

## Rename Columns
```Python
import pandas as pd
df = pd.Dataframe(
    "fur_color": ["grey", "grey", "white", "black"],
    "size_in_cm": [100, 150, 100, 80]
)

df.rename(columns = {"fur_color":"COLOR", "size_in_cm":"SIZE"}, inplace = True)
```

|   | COLOR | SIZE |
|---|-------|------|
| 0 | grey  | 100  |
| 1 | grey  | 150  |
| 2 | white | 100  |
| 3 | black | 80   |

## Columns (Values) to Dictionnaries
```Python
import pandas as pd
df = pd.Dataframe(
    "temperature": ["cold", "warm"],
    "region": ["Taiga", "Desert"]
)
```

|   | temperature | region |
|---|-------------|--------|
| 0 | cold        | Taiga  |
| 1 | warm        | Desert |

```Python
dict_from_cols = pd.Series(df.temperatures, index=df.region).to_dict()

# dict_from_cols = {"Taiga":"cold", "Desert":"warm"}
```

## Add a new Column via a dictionnary (according to preexisting dataset) [Mapping]
```Python
import pandas as pd
df = pd.Dataframe(
    "temperature": ["cold", "warm"],
    "region": ["Taiga", "Desert"]
)
```

|   | temperature | region |
|---|-------------|--------|
| 0 | cold        | Taiga  |
| 1 | warm        | Desert |

```Python
region_tag_dict = {"Taiga": "TG", "Desert":"DS"}

df["region_tag"] = df["region"].map(region_tag_dict)
```

|   | temperature | region | region_tag |
|---|-------------|--------|------------|
| 0 | cold        | Taiga  | TG         |
| 1 | warm        | Desert | DS         |

## Combinations & Value counts

### **unique Values per element & count**
```Python
import pandas as pd
df = pd.Dataframe(
    "fur_color": ["grey", "grey", "white", "black"],
    "size_in_cm": [100, 150, 100, 80]
)

color_spread = df["fur_color"].value_counts()
```

|       | fur_color |
|-------|-----------|
| grey  | 2         |
| white | 1         |
| black | 1         |

### **unique Values 2 rows together & count**
```Python
import pandas as pd
df = pd.Dataframe(
    "fur_color": ["grey", "grey", "white", "black"],
    "size_in_cm": [100, 150, 100, 80]
)

two_columns_combination = pd.crosstab(df.fur_color,df.size_in_cm)
```

|       | 80 | 100 | 150 |
|-------|----|-----|-----|
| grey  | 0  | 1   | 1   |
| white | 0  | 1   | 0   |
| black | 1  | 0   | 0   |

## Flask

## Plotly

## Dash