
---

### **analysis.py**
```python
import pandas as pd

def analyze_data(file_path):
    df = pd.read_csv(file_path)
    summary = df.describe()
    print(summary)
    return summary

if __name__ == "__main__":
    analyze_data("data.csv")
